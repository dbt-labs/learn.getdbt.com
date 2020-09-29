# Working Group #1

**Facilitation Guide** The instructor should be driving for most of this session.  Be sure to allow people time to catch up after each step outlined below.

**Working Process** - Facilitate discussion to name the following steps for building the orders model and refactoring the customers model
1. Inspect `raw.stripe.payment`
2. Stage payment data as `stg_payments`
3. Inspect `stg_payments` and `stg_orders`, recognize that orders to payments is one-to-many.
4. Write the `orders` model
5. Refactor the `customers` model

**`stg_payments.sql`**
```sql
select
    id as payment_id,
    orderid as order_id,
    paymentmethod as payment_method,
    status,

    -- amount is stored in cents, convert it to dollars
    amount / 100 as amount,
    created as created_at

from raw.stripe.payment
```

**`orders.sql`**
```sql
with orders as  (
    select * from {{ ref('stg_orders' )}}
),

payments as (
    select * from {{ ref('stg_payments') }}
),

order_payments as (
    select
        order_id,
        sum(case when status = 'success' then amount end) as amount

    from payments
    group by 1
),

final as (

    select
        orders.order_id,
        orders.customer_id,
        orders.order_date,
        orders.status,
        coalesce(order_payments.amount, 0) as amount

    from orders
    left join order_payments using (order_id)
)

select * from final

```

**`customers.sql (refactored)`**
```sql
with customers as (

    select * from {{ ref('stg_customers') }}

),

orders as (

    select * from {{ ref('orders') }}

),

customer_orders as (

    select
        customer_id,

        min(order_date) as first_order_date,
        max(order_date) as most_recent_order_date,
        count(order_id) as number_of_orders,
        sum(amount) as lifetime_value

    from orders

    group by 1

),


final as (

    select
        customers.customer_id,
        customers.first_name,
        customers.last_name,
        customer_orders.first_order_date,
        customer_orders.most_recent_order_date,
        coalesce(customer_orders.number_of_orders, 0) as number_of_orders,
        customer_orders.lifetime_value

    from customers

    left join customer_orders using (customer_id)

)

select * from final
```

# Working Group #2

**Facilitation Guide** Ask people how they want to work by sending you a private message in Zoom chat:
(1) Independently then check in towards the end
(2) Guided with a screen share

**Working Process** - Facilitate discussion to name the following steps for building the orders model and refactoring the customers model
1. Add Tests
2. Add Sources and Refactor
3. Add Docs
4. Refactor project into marts/core and staging


**`src_jaffle_shop.yml`**
```yml
version: 2

sources:
  - name: jaffle_shop
    description: A replica of the postgres database
    database: raw
    tables:
      - name: customers
        columns:
          - name: id
            tests:
              - unique
              - not_null

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

          - name: status
            description: "{{ doc('order_status') }}"
            tests:
              - accepted_values:
                  values: ['placed', 'shipped', 'completed', 'return_pending', 'returned']

          - name: user_id
            description: Foreign key to customers
            tests:
              - not_null
              - relationships:
                  to: source('jaffle_shop', 'customers')
                  field: id
```

**`stg_jaffle_shop`**
```yml
version: 2

models:
  - name: stg_customers
    columns:
      - name: customer_id
        tests:
          - unique
          - not_null

  - name: stg_orders
    columns:
      - name: order_id
        tests:
          - unique
          - not_null

      - name: status
        tests:
          - accepted_values:
              values: ['placed', 'shipped', 'completed', 'return_pending', 'returned']

      - name: customer_id
        tests:
          - not_null
          - relationships:
              to: ref('stg_customers')
              field: customer_id
```

**`core.yml`**
```yml
version: 2

models:

  - name: dim_customers
    columns:
      - name: customer_id
        tests:
          - unique
          - not_null

  - name: fct_orders
    description: One record per order
    columns:
      - name: order_id
        tests:
          - unique
          - not_null
      - name: status
        description: "{{ doc('order_status') }}"
        tests:
          - accepted_values:
              values: ['placed', 'shipped', 'completed', 'return_pending', 'returned']

      - name: amount
        description: Amount in USD
```

# Working Group #3
(tbd)

# Working Group #4
(tbd)