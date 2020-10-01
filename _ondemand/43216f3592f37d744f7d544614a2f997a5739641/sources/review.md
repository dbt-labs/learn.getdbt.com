---
layout: lesson
module: Sources
moduleSlug: sources
title: Review
---

# Review

**Sources**
* As established in the Modeling modules, sources represent the raw data that has been loading into the Data Warehouse.
* We *can* always reference tables in our models with the explicit table name (`raw.jaffle_shop.customers`).
* Setting up Sources in dbt enables a few other important tools:
    * Multiple tables from a single sources can be configured in one place.  The source macro will then select this updated naming convention.
    * Sources will be rendered in the DAG when viewing documentation.
    * Text and Doc Block can be used to add decriptions to sources.
    * Tests can be run directly on sources before staging.
    * Snapshot-Freshness for checking the freshness of raw tables.

**Configuring Sources**
* Sources are configured in dbt in YML files in the models directory.
* The following code block configures the table `raw.jaffle_shop.customers` and `raw.jaffle_shop.orders`:

```yml
version: 2

sources:
  - name: jaffle_shop
    database: raw
    tables:
      - name: customers
      - name: orders
```

* The full documentation for configuring sources can be found in the [source properties](https://docs.getdbt.com/reference/source-properties) page in the docs.

**Source Macro**
* The `ref` macro is used to build dependencies from one model to another.
* The `source` macros similarly is used to build a dependency between one model to a source.
* Given the source configuration above, the {% raw %} `{{ source('jaffle_shop','customers') }}` {% endraw %} in a model file would compile to `raw.jaffle_shop.customers`

**Documenting and Testing Sources**
* Documentation and Tests are configured for models in YML files - the same is true for sources.
* In the same YML file where the sources was configured, descriptions and tests can be added.  Descriptions can be added on the source, table, and column level.

```yml
version: 2

sources:
  - name: jaffle_shop
    description: A replica of a Postgres Database
    database: raw
    tables:
      - name: customers
        description: Raw customers data
        columns:
          - name: id
            description: Primary key for customers
      - name: orders
```
* When the documentation is generrated, sources will be documented as well.
* The DAG will represent the sources in green.

<img src="/ui/img/ondemand/DAG_sources.png" style="width: 80%; margin: auto">

**Snapshotting Source Freshness**
* Freshness thresholds can be set in the YML file where sources are configured.  For each table, the keys `loaded_at_field` and `freshness` must be configured.

```yml
version: 2

sources:
  - name: jaffle_shop
    description: A replica of the postgres database
    database: raw
    tables:
      - name: orders
        loaded_at_field: _etl_loaded_at
        freshness:
          warn_after: {count: 12, period: hour}
          error_after: {count: 24, period: hour}
        columns:
          - name: id
            tests:
              - unique
              - not_null
```

* A threshold can be configured for giving a warning and an error with the keys `warn_after` and `error_after`.
* The freshness of sources can then be determine with the command `dbt source snapshot-freshness`.