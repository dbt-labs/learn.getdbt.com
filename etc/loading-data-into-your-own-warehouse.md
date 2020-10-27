# Loading data into your own warehouse
The data used in this tutorial is stored as CSVs in a public S3 bucket.

We've included instructions for loading this data into a Snowflake warehouse

## Snowflake
These instructions assume:
- You have a database named `raw`
- You have the correct privileges to create in that database

If this is not the case, you may have to amend the SQL you run to use a database
that you have "create" privileges on.

```sql
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

## BigQuery
Use the publicly available data:
```sql
select * from `dbt-tutorial.jaffle_shop.customers`;
select * from `dbt-tutorial.jaffle_shop.orders`;
select * from `dbt-tutorial.stripe.payment`;
```

## Other warehouses
We recommend that if you're using another warehouse (Redshift, Postgres, etc),
or do not have the correct privileges to load data into your Snowflake warehouse,
you should use the BigQuery version of this tutorial.

Alternatively, if you're experienced with loading data into a warehouse from an S3 bucket,
feel free to amend the above DDL to work on your warehouse.
