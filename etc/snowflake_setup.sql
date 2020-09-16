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
  status varchar,
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
-- ❗️This part needs to be run from the Fishtown Snowflake account
use role accountadmin
create share if not exists learn;
grant usage on database analytics to share learn;
-- grant reference_usage on database raw to share learn; --CC note: limited success so far
alter share learn add accounts = fka50167;

/* Then, add views to the share as models in our dbt project (check out the
`anonymized_ticket_tailor__orders` model as an example)

The view must _only_ select from tables within the same database. Theoretically
we should be able to grant reference usage to work around this, however I
haven't had any luck doing that.
*/

-- ❗️This part needs to be run from the Learn Snowflake account
use role accountadmin;
create database if not exists share_fishtown_analytics  from share kw27752.learn;
grant imported privileges on database share_fishtown_analytics to role transformer;

use role loader;
create schema if not exists raw.ticket_tailor;
-- for each table:
create view raw.ticket_tailor.orders as (
    select * from share_fishtown_analytics.shared_ticket_tailor.orders
);
-- etc.
-- NB: the transformer role should inherit privileges automatically, but it's worth checking
use role transformer;
-- for each table, confirm that the transformer can read it
select * from raw.ticket_tailor.orders;

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
