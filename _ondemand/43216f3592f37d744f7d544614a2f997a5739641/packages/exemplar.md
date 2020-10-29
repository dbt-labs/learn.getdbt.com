---
layout: lesson
module: Packages
moduleSlug: packages
title: Exemplar
---

## Exemplar

`packages.yml` in the root directory of your project

```
packages:
  - package: fishtown-analytics/dbt_utils
    version: 0.6.2
```

`all_dates.sql` in the `models` folder

{% raw %}
```
{{ config (
    materialized="table"
)}}

{{ dbt_utils.date_spine(
    datepart="day",
    start_date="to_date('01/01/2020', 'mm/dd/yyyy')",
    end_date="to_date('01/01/2021', 'mm/dd/yyyy')"
   )
}}
```
{% endraw %}