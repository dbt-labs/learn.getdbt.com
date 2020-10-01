---
layout: lesson
module: Analyses and Seeds
moduleSlug: analyses-seeds
---

# Review

### Analyses
* Analyses are .sql files that live in the analyses folder.
* Analyses will not be run with `dbt run` like models.  However, you can still compile these from Jinja-SQL to pure SQL using `dbt compile`.  These will compile to the target folder.
* Analyses are useful for training queries, one-off queries, and audits

### Seeds
* Seeds are .csv files that live in the data folder.
* HWne executing `dbt run`, seeds will be built in your Data Warehouse as tables.
Seeds can be references using the `ref` macro - just like models!
* ✅ Seeds **should** be used for data that doesn't change frequently.
* ⛔️ Seeds **should not** be the process for uploading data that changes frequently
* Seed are useful for loading country codes, employee emails, or employee account IDs
    * Note: If you have a rapidly growing or large company, this may be better addressed through an orchestrated loading solution.