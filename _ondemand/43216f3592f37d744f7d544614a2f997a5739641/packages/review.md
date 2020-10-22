---
layout: lesson
module: Packages
moduleSlug: packages
title: Review
render_with_liquid: false
---

# Review

**Packages** are a tool for importing models and macros into your dbt Project.  These may have been written in by a coworker or someone else in the dbt community that you have never met.  Fishtown Analytics maintains a site called hub.getdbt.com for sharing open-source packages that you can install in your project.  Packages can also be imported directly from GitHub, GitLab, or another site or from a subfolder in your dbt project.

**Installing Packages**
- Packages are configured in the root of your dbt project in a file called ‘packages.yml’
- You can adjust the version to be compatible with your working version of dbt.  Read the packages documentation to determine the version to use.
- Packages are then installed with the command `dbt deps`

**Example: Adding dbt_utils and snowflake_spend to your dbt project**

`Packages.yml`
```
packages:
  - package: fishtown-analytics/dbt_utils
    version: 0.6.2
  - package: gitlabhq/snowflake_spend
    version: 1.2.0
```

`dbt deps`



**Using Macros from a Package**
- After importing a package, your dbt project now has access to all the macros from that package.
- The documentation of that particular package is the best place to learn how to use those packages.
- When you want to reference a macro in a package, you must reference that package and then select the particular macro. (e.g. `dbt_utils.data_spine’)

**Example - The following snippet will reference the dbt_utils package and use the date_spine macro.**
```
{{ dbt_utils.date_spine(
    datepart=”day”
    start_date=”to_date(‘01/01/2016’, ‘mm/dd/yyyy’)”,
    End_date=”dateadd(week, 1, current_date)”
    )
}}
```
**Using Models from a Package**
- After importing a package, your dbt project now has access to all the models from that package.
- The documentation of that particular packages is the best place to learn how to use those packages.
- Those models will then become part of your dbt project.  They will be build when you run dbt run and can be viewed in documentation as part of your DAG and text-based documentation as well.

**Example - The following DAG below shows all of the snowflake_spend model in gray**

<img src="/ui/img/ondemand/snowflake_spend_dag.png" style="width: auto; margin: auto; max-height: 500px">


