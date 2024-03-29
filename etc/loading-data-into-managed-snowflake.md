# Loading data into a managed Snowflake account

These are the instructions for loading data into a Snowflake account that we
manage, for example, the dedicated `learn` Snowflake account.

### 1. Setup roles, databases, and privileges

[ To Do ]


### 2. Load CSV data from S3 into tables
We do a simple copy from S3 into tables here. We want to show off how source
freshness works in this course, so for some of the tables, we then create a
view on top of the table with a calculated freshness column, so that it's always
up-to-date.

For these views, we hid the actual table in a very sneaky schema named "do_not_look",
so that the Learn students would just see the one "orders" table in the schema
instead of two. Curious students look in the "do_not_look" schema, but we are ok
with them looking under the hood!

```sql
use role loader;
create schema raw.do_not_look;
create schema raw.jaffle_shop;

-- create this one directly in the schema
create table raw.jaffle_shop.customers
(
    id integer,
    first_name varchar,
    last_name varchar
);

copy into raw.jaffle_shop.customers from 's3://dbt-tutorial-public/jaffle_shop_customers.csv'
    file_format = (
        type = 'CSV'
        field_delimiter = ','
        skip_header = 1
    )
;

-- create this in the "do not look" schema so we can add a _batched_at column
create or replace table raw.do_not_look.orders
(
  id integer,
  user_id integer,
  order_date date,
  status varchar
);

copy into raw.do_not_look.orders from 's3://dbt-tutorial-public/jaffle_shop_orders.csv'
    file_format = (
        type = 'CSV'
        field_delimiter = ','
        skip_header = 1
    )
;

create or replace view raw.jaffle_shop.orders as (
    select
        *,
        dateadd(hour, -16, current_timestamp) as _etl_loaded_at

    from raw.do_not_look.orders
);

create schema raw.stripe;

create or replace table raw.do_not_look.payment (
  id integer,
  orderid integer,
  paymentmethod varchar,
  status varchar,
  amount integer,
  created date
);

copy into raw.do_not_look.payment from 's3://dbt-tutorial-public/stripe_payments.csv'
    file_format = (
        type = 'CSV'
        field_delimiter = ','
        skip_header = 1
    )
;

create or replace view raw.stripe.payment as (
    select
        *,
        dateadd('hour', -4, current_timestamp) as _batched_at
    from raw.do_not_look.payment
);

```

## 3. Setup Snowflake Shares
We share data from our main Fishtown account to the Learn account.

**From the Fishtown account**, we ran:
```sql
-- ❗️This part needs to be run from the Fishtown Snowflake account
use role accountadmin
create share if not exists learn;
grant usage on database analytics to share learn;
grant reference_usage on database raw to share learn;
alter share learn add accounts = fka50167;

/* Then, add secure views to the share as models in our dbt project (check out the
`anonymized_ticket_tailor__orders` model as an example)
*/
```

Then, **from the learn account**, we ran:
```sql
-- ❗️This part needs to be run from the Learn Snowflake account
use role accountadmin;
create database if not exists share_fishtown_analytics  from share kw27752.learn;
grant imported privileges on database share_fishtown_analytics to role transformer;

use role loader;
create schema if not exists raw.ticket_tailor;
-- for each table:
create view raw.ticket_tailor.orders as (
    select * from share_fishtown_analytics.shared_ticket_tailor.orders
);
-- etc.
-- NB: the transformer role should inherit privileges automatically, but it's worth checking
use role transformer;
-- for each table, confirm that the transformer can read it
select * from raw.ticket_tailor.orders;
```

# 4. Create users

Use the `setup-learn.py` script to do this
