---
layout: lesson
module: Models
moduleSlug: models
title: Reorganize Project
---

{% include options/ondemand/wistia_embed.html %}

#### Reference: Reorganized File Structure

*Note: You will see `logs` and `target` if after you run `dbt run` for the first time.  You will not see `dbt_modules` if you have not imported a package yet (more on this in the packages module)

```
dbt-learn
├── analysis
├── dbt_modules
├── logs
├── macros
├── models
    └── marts
        └── core
            └── dim_customers.sql  
    └── staging
        └── jaffle_Shop
            ├── stg_customers.sql
            └── stg_orders.sql 
├── snapshots
├── target
├── tests
├── .gitignore
├── dbt_project.yml
└── README.md
```