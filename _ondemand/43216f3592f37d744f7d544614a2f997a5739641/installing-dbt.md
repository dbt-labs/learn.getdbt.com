---
layout: overview
title: Installing dbt
learningObjectives:
  - Installing/Setting up dbt
  - Configure your connection to your warehouse.
  - Configure your connection to your repository.
---

# Installing/Setting up 
Currently dbt can be used in two different ways:
* Locally on your machine through the **Command line interface**
* Through your browser through **dbt Cloud**

Choose the video below that best matches your use case:

## CLI on Mac
<!-- embed video here -->

## CLI on Windows
<!-- embed video here -->

## dbt Cloud
<!-- embed video here -->

# Installing git
dbt Cloud is already set up with git for version control.  If you are developing locally, you will need to install git on your machine.  

Choose the video below that best matches your use case:

## CLI / Mac / git

## CLI / Windows / git

# Connecting to your warehouse
Now that you have gotten set up with dbt, it is time to configure your connection to the warehouse.  Currently, dbt supports Snowflake, Big Query, Redshift, and Postgres.  If you are using a different Data Warehouse, please consider the [community supported adapters](https://docs.getdbt.com/docs/supported-databases).

Choose the video below that best matches your use case:

## CLI / Mac / Snowflake
<!-- embed video here -->

## CLI / Mac / Big Query
<!-- embed video here -->

## CLI / Mac / Redshift
<!-- embed video here -->

## CLI / Mac / Postgres
<!-- embed video here -->

## CLI / Windows / Snowflake
<!-- embed video here -->

## CLI / Windows / Big Query
<!-- embed video here -->

## CLI / Windows / Redshift
<!-- embed video here -->

## CLI / Windows / Postgres
<!-- embed video here -->

## dbt Cloud / Snowflake
<!-- embed video here -->

## dbt Cloud / Big Query
<!-- embed video here -->

## dbt Cloud / Redshift
<!-- embed video here -->

## dbt Cloud / Postgres
<!-- embed video here -->

# Connecting to your repository
We are almost there!  Now we need to connection to a remote repository so we can leverage **Version Control** in our analytics workflow.  Any git provider will work with a a given git URL.  If you have an existing dbt_project, you can simply add that.  However, if you are starting from scratch, you will need an brand new repository with no commits - no even a README file.

## CLI / Git

## dbt Cloud
