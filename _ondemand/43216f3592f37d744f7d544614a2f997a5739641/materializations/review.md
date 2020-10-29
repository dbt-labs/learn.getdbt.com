---
layout: lesson
module: Materializations
moduleSlug: materializations
title: Review
---

## Review

**Tables**

- Built as tables in the database
- Data is stored on disk
- Slower to build
- Faster to query
- Configure in dbt_project.yml or with the following config block

{% raw %}

```
{{ config(
    materialized='table'
)}}
```
{% endraw %}

**Views**

- Built as views in the database
- Query is stored on dick
- Faster to build
- Slower to query
- Configure in dbt_project.yml or with the following config block

{% raw %}

```
{{ config(
    materialized='view'
)}}
```
{% endraw %}

**Ephemeral**

- Does not exist in the database
- Imported as CTE into downstream models
- Increases build time of downstream models
- Cannot query directly
- [Ephemeral Documentation](https://docs.getdbt.com/docs/building-a-dbt-project/building-models/materializations#ephemeral)
- Configure in dbt_project.yml or with the following config block

{% raw %}

```
{{ config(
    materialized='ephemeral'
)}}
```
{% endraw %}

**Incremental Models**

- Built as table in the database
- On the first run, builds entire table
- On subsequent runs, only appends new records*
- Faster to build because you are only adding new records
- Does not capture 100% of the data all the time
- [Incremental Documentation](https://docs.getdbt.com/docs/building-a-dbt-project/building-models/materializations#incremental)
- [Discourse post on Incrementality](https://discourse.getdbt.com/t/on-the-limits-of-incrementality/303)
- Configuration is more advanced in this case.  Consult the dbt documentation for building your first incremental model.

**Snapshots**

- Built as a table in the database, usually in a dedicated schema.
- On the first run, builds entire table and adds four columns: `dbt_scd_id`, `dbt_updated_at`, `dbt_valid_from`, and `dbt_valid_to`
- In future runs, dbt will scan the underlying data and append new records based on the configuration that is made.
- This allows you to capture historical data
- [Snapshots Documentation](https://docs.getdbt.com/docs/building-a-dbt-project/snapshots)
- Configuration is more advanced in this case.  Consult the dbt documentation for writing your first snapshot.

