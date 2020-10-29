# Loading data into BigQuery
This is how data came to exist in BigQuery for the public Getting Started tutorial

## 1. Create a BigQuery project
We have a project named `dbt-tutorial` that is in the `fishtownanalytics.com`
GCP account. Both Claire and Drew are owners of this.

## 2. Create a staging dataset
Using the [BigQuery console](https://console.cloud.google.com/bigquery?project=dbt-tutorial&folder=&supportedpurview=project):
1. Download each of the tables from S3 by visiting:
  - http://dbt-tutorial-public.s3-us-west-2.amazonaws.com/jaffle_shop_orders.csv
  - http://dbt-tutorial-public.s3-us-west-2.amazonaws.com/jaffle_shop_customers.csv
  - http://dbt-tutorial-public.s3-us-west-2.amazonaws.com/stripe_payments.csv

2. Edit the files so they have lower-case column names
3. Create a `dataset` named `data_prep`
4. Create a table for each data source by using the "create table" UI, and uploading the CSV manually.

## 3. Create final datasets
1. Use the BigQuery UI to create two new datasets, `jaffle_shop` and `stripe`.

2. Use SQL to create views:

```sql
create or replace view jaffle_shop.customers as (
    select * from data_prep.jaffle_shop_customers
);

create or replace view jaffle_shop.orders as (
    select
        *,
        datetime_add(current_datetime, interval -16 hour) as _etl_loaded_at

    from data_prep.jaffle_shop_orders
);

create view stripe.payment as (
      select
        *,
        datetime_add(current_datetime, interval -4 hour) as _batched_at
    from data_prep.stripe_payments
);

```

## 4. Grant permissions
3. For each dataset, grant permissions so that everyone can read this data by using the `share dataset` button:
    - Add "AllUsers" to the Viewer role
    - Add "AllAuthenticatedUsers" to the Viewer role
