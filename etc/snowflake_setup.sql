-- PART ONE: SETUP ROLES, DATABASES AND PRIVILIGES
-- [ to-do ]

-- PART TWO: SETUP SIMPLE DATA SOURCES
/*
We do a simple copy from S3 into tables here. We want to show off how source
freshness works in this course, so for some of the tables, we then create a
view on top of the table with a calculated freshness column, so that it's always
up-to-date.

For these views, we hid the actual table in a very sneaky schema named "do_not_look",
so that the Learn students would just see the one "orders" table in the schema
instead of two. Curious students look in the "do_not_look" schema, but we are ok
with them looking under the hood!
*/

use role loader;
create schema raw.do_not_look;
create schema raw.jaffle_shop;

-- create this one directly in the schema
create table raw.jaffle_shop.customers
(
    id integer,
    first_name varchar,
    last_name varchar
);

copy into raw.jaffle_shop.customers from 's3://dbt-tutorial-public/jaffle_shop_customers.csv'
    file_format = (
        type = 'CSV'
        field_delimiter = ','
        skip_header = 1
    )
;

-- create this in the "do not look" schema so we can add a _batched_at clumn
create or replace table raw.do_not_look.orders
(
  id integer,
  user_id integer,
  order_date date,
  status varchar
);

copy into raw.do_not_look.orders from 's3://dbt-tutorial-public/jaffle_shop_orders.csv'
    file_format = (
        type = 'CSV'
        field_delimiter = ','
        skip_header = 1
    )
;

create or replace view raw.jaffle_shop.orders as (
    select
        *,
        dateadd(hour, -16, current_timestamp) as _etl_loaded_at

    from raw.do_not_look.orders
);

create schema raw.stripe;

create or replace table raw.do_not_look.payment (
  id integer,
  orderID integer,
  paymentMethod varchar,
  amount integer,
  created date
);

copy into raw.do_not_look.payment from 's3://dbt-tutorial-public/stripe_payments.csv'
    file_format = (
        type = 'CSV'
        field_delimiter = ','
        skip_header = 1
    )
;

create or replace view raw.stripe.payment as (
    select
        *,
        dateadd('hour', -4, current_timestamp) as _batched_at
    from raw.do_not_look.payment
);


-- PART THREE: SETUP SNOWFLAKE SHARES
-- [ to-do ]

-- PART FOUR: ADD USERS
-- For each attendee we run the following:
/*
create user learner_hperson
    password = 'ChangeMe123'
    must_change_password = true
    default_role = transformer
    default_warehouse = transforming
    comment = 'dbt Learn 2020-04-09'
    days_to_expiry = 30 -- ~ two weeks after course, given we create this ~2 weeks before course;

grant role transformer to user learner_hperson;
*/
