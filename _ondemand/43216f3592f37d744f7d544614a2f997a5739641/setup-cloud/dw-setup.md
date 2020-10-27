---
layout: lesson
module: Set up dbt Cloud
moduleSlug: setup-cloud
title: Data Warehouse Set Up

---

# Loading Data in your own Warehouse for Training

Currently dbt Cloud supports Postgres, Redshift, BigQuery, and Snowflake.

The data used in this course are stored as CSVs in a public S3 bucket. You may use the following URLs to import these tables into your data warehouse for your own use:

```
http://dbt-tutorial-public.s3-us-west-2.amazonaws.com/jaffle_shop_orders.csv
http://dbt-tutorial-public.s3-us-west-2.amazonaws.com/jaffle_shop_customers.csv
http://dbt-tutorial-public.s3-us-west-2.amazonaws.com/stripe_payments.csv
```

We have provided guidance and code snippets below for a) querying this public data in BigQuery and b) importing this data into your own Snowflake database.

If you are unsure of where to start, we recommend using BigQuery.  BigQuery offers a generous free tier and supports public data sets.  This will allow you to avoid loading this training data on your own.

## BigQuery

BigQuery supports public data sets that can be direclty queried.  The data is publically available with the following select statements.  This will be important for reference in the `models` and `sources` modules.

```
select * from `dbt-tutorial.jaffle_shop.customers`;
select * from `dbt-tutorial.jaffle_shop.orders`;
select * from `dbt-tutorial.stripe.payment`;
```

## Snowflake

The instructions below assume that you have a database named `raw` in your Snowflake account and you have the correct privleges to create objects in this database.

If this is not the case, you may need to modify the query below for a database that these prerequisites do apply.

Run the following commands in your Snowflake Warehouse SQL Runner:

```
create schema raw.jaffle_shop;

-- create this one directly in the schema
create table raw.jaffle_shop.customers
(
    id integer,
    first_name varchar,
    last_name varchar
);

copy into raw.jaffle_shop.customers (id, first_name, last_name)
    from 's3://dbt-tutorial-public/jaffle_shop_customers.csv'
        file_format = (
            type = 'CSV'
            field_delimiter = ','
            skip_header = 1
        )
;

create table raw.jaffle_shop.orders
(
  id integer,
  user_id integer,
  order_date date,
  status varchar,
  _etl_loaded_at timestamp default current_timestamp
);

copy into raw.jaffle_shop.orders (id, user_id, order_date, status)
    from 's3://dbt-tutorial-public/jaffle_shop_orders.csv'
        file_format = (
            type = 'CSV'
            field_delimiter = ','
            skip_header = 1
        )
;

create schema raw.stripe;

create table raw.stripe.payment (
  id integer,
  orderid integer,
  paymentmethod varchar,
  status varchar,
  amount integer,
  created date,
  _batched_at timestamp default current_timestamp
);

copy into raw.stripe.payment (id, orderid, paymentmethod, status, amount, created)
from 's3://dbt-tutorial-public/stripe_payments.csv'
    file_format = (
        type = 'CSV'
        field_delimiter = ','
        skip_header = 1
    )
;
```

Now that you have the training data in your data warehouse, we can start setting up your GitHub repository.