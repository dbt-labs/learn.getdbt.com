---
layout: lesson
module: Sources
moduleSlug: sources
title: Practice
---

# Practice 
Using the resources in this module, complete the following in your dbt project:

**Configure Sources:**
- Configure a source for the tables `raw.jaffle_shop.customers` and `raw.jaffle_shop.orders` in a file called `src_jaffle_shop.yml`

**`models/staging/jaffle_shop/src_jaffle_shop`**

```
version: 2

sources:
    - name: jaffle_shop
      database: raw
      tables:
        - name: customers
        - name: orders
```

- (Open ended*) Configure a source for the tables `raw.stripe.payment` in a file called `src_stripe.yml`

**Refactor Staging Models:**
- Refactor `stg_customers` using the source macro.

**`models/staging/jaffle_shop/stg_customers`**

{% raw %}
```
select 
    id from customer_id,
    first_name,
    last_name
from {{ source('jaffle_shop','customers') }}
```
{% endraw %}

- Refactor `stg_orders` using the source macro.

**`models/staging/jaffle_shop/stg_orders`**

{% raw %}
```
select
    id as order_id,
    user_id as customer_id,
    order_date,
    status
from {{ source('jaffle_shop','orders') }}
```
{% endraw %}

- (Open-ended*) Refactor `stg_payments` using the source macro 

**Add Documentation and Tests:**
- Add documentation at the model and table level of your tables.
- Add `unique` and `not_null` tests to the ID's in each of your sources

**models/staging/jaffle_shop/src_jaffle_shop**

```
version: 2

sources:
    - name: jaffle_shop
      description: A clone of a Postgres application database.
      database: raw
      tables:
        - name: customers
          description: Raw customers data.
          columns:
            - name: id
              description: Primary key for customers
              tests:
                - unique
                - not_null

        - name: orders
          description: Raw orders data.
          columns:
            - name: id
              description: Primary key for orders.
              tests:
                - unique
                - not_null
```


**Review Documentation:**
- Generate documentation to view the sources in your DAG using `dbt docs generate`

**Extra Credit:**
- Configure your Stripe payments data to check for source freshness.
- Run snapshot-freshness.

* Check the exemplar on the next page for the open ended exercises