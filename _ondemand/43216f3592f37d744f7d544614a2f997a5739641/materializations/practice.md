---
layout: lesson
module: Materializations
moduleSlug: materializations
title: Practice
---

# Practice

#### Tables, Views, and Ephemeral Models

To gain a deeper understanding of tables, views, and ephemeral models, try making the following changes to your project.  However, don't commit these changes to your git repository.  Use this solely as a change to experiment with these materializatons.

#### Incremental Models
Try the following steps that were covered in the video to build your own incremental model.

- Configure a new source in the folder `models/staging/snowplow` called `src_snowplow.yml`.

```
version: 2
sources:
  - name: snowplow
    database: raw
    loaded_at_field: collector_tstamp
    freshness:
      error_after: {count: 1, period: hour}
    tables:
      - name: events
```

- Create an incremental model with the following code snippet in the folder `models/staging/snowplow` called `stg_page_views.sql`.

{% raw %}
```
{{ config(
    materialized = 'incremental',
    unique_key = 'page_view_id'
) }}
with events as (
    select * from {{ source('snowplow', 'events') }}
    {% if is_incremental() %}
    where collector_tstamp >= (select max(max_collector_tstamp) from {{ this }})
    {% endif %}
),
page_views as (
    select * from events
    where event = 'page_view'
),
aggregated_page_events as (
    select
        page_view_id,
        count(*) * 10 as approx_time_on_page,
        min(derived_tstamp) as page_view_start,
        max(collector_tstamp) as max_collector_tstamp
    from events
    group by 1
),
joined as (
    select
        *
    from page_views
    left join aggregated_page_events using (page_view_id)
)
select * from joined
```
{% endraw %}

- Run the incremental model for the first time by running `dbt run -m stg_page_views`.
- Navigate to [learn.getdbt.com/lessons/incremental](learn.getdbt.com/lessons/incremental) and click through the slides to add page views.
- After about 10 minutes or so execute `dbt run -m stg_page_views` and your incremental model will process an incremental build.  Take a look at the logs to see the DDL/DML used to build this model incrementally.
- Rebuild the entire model again by running `dbt run --full-refresh`

#### Snapshots
Snapshots are difficult to practice without genuine type 2, slowly changing dimension data.  We are working on a way to make this more authentic for our learning environment.  For this exercise, use the following code snippets to practice snapshots.

- **(In Snowflake)** Create a table called mock_orders in your development schema.  You will have to replace `dbt_kcoapman` in the snippet below.

```
create or replace transient table analytics.dbt_kcoapman.mock_orders (
  order_id integer,
  status varchar (100),
  created_at date,
  updated_at date
);
```


- **(In Snowflake)** Insert values into the mock_orders table in your development schema.  You will have to replace `dbt_kcoapman` in the snippet below.

```
insert into analytics.dbt_kcoapman.mock_orders (order_id, status, created_at, updated_at)
values (1, 'delivered', '2020-01-01', '2020-01-04'),
       (2, 'shipped', '2020-01-02', '2020-01-04'),
       (3, 'shipped', '2020-01-03', '2020-01-04'),
       (4, 'processed', '2020-01-04', '2020-01-04');
```

- **(In dbt Cloud)** Create a new snapshot in the folder `snapshots` with the filename `mock_orders.sql` with the following code snippet.  Note: Jinja is being used here to create a new, dedicated schema.

{% raw %}
```
{% snapshot mock_orders %}

{% set new_schema = target.schema + '_snapshot' %}

{{
    config(
      target_database='analytics',
      target_schema=new_schema,
      unique_key='order_id',

      strategy='timestamp',
      updated_at='updated_at',
    )
}}

select * from analytics.{{target.schema}}.mock_orders

{% endsnapshot %}
```
{% endraw %}

- **(In dbt Cloud)** Run snapshots by executing `dbt snapshot`.

- **(In dbt Cloud)** Run the following snippet in a statement tab to see the current snapshot table.  You will have to replace `dbt_kcoapman` with your development schema.  Take note of how dbt has added three columns.

```
select * from analytics.dbt_kcoapman_snapshot.mock_orders
```

- **(In Snowflake)** Recreate a table called mock_orders in your development schema.  You will have to replace `dbt_kcoapman` in the snippet below.

```
create or replace transient table analytics.dbt_kcoapman.mock_orders (
  order_id integer,
  status varchar (100),
  created_at date,
  updated_at date
);
```

- **(In Snowflake)** Insert these new values into the mock_orders table in your development schema.  You will have to replace `dbt_kcoapman` in the snippet below.

```
insert into analytics.dbt_kcoapman.mock_orders (order_id, status, created_at, updated_at)
values (1, 'delivered', '2020-01-01', '2020-01-05'),
       (2, 'delivered', '2020-01-02', '2020-01-05'),
       (3, 'delivered', '2020-01-03', '2020-01-05'),
       (4, 'delivered', '2020-01-04', '2020-01-05');
```

- **(In dbt Cloud)** Re-run snapshots by executing `dbt snapshot`.

- **(In dbt Cloud)** Run the following snippet in a statement tab to see the current snapshot table.  You will have to replace `dbt_kcoapman` with your development schema.  Now take not of how dbt has 'snapshotted' the data to capture the changes over time!

```
select * from analytics.dbt_kcoapman_snapshot.mock_orders
```

Note: If you want to start this process over, you will need to drop the snapshot table by running the following in Snowflake.  This will force dbt to create a new snapshot table in step 4.  (Again, you will need ot swap in your development schema for `dbt_kcoapman`)

```
drop table analytics.dbt_kcoapman_snapshot.mock_orders
```



