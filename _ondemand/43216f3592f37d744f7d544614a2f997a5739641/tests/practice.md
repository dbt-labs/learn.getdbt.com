---
layout: lesson
module: Tests
moduleSlug: tests
title: Practice
---

# Practice 
Using the resources in this module, complete the following exercises in your dbt project:

**Schema Tests:**
- Add tests to your jaffle_shop staging tables:
    - Create a file called `stg_jaffle_shop.yml` for congfiguring your tests
    - Add `unique` and `not_null` tests to the keys for each of your staging tables
    - Add an `accepted_values` test to your `stg_orders` model for status.
    - Run your tests

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
        - name: status
          tests:
            - accepted_values:
                values:
                  - completed
                  - shipped
                  - returned
                  - placed
                  - return_pending
```

**Data Tests:**
- Add the test `tests/assert_positive_value_for_total_amount` to be run on your `stg_payments` model.
- Run your tests

{% raw %}
```
-- Refunds have a negative amount, so the total amount should always be >= 0.
-- Therefore return records where this isn't true to make the test fail.
select
    order_id,
    sum(amount) as total_amount
from {{ ref('stg_payments') }}
group by 1
having not(total_amount >= 0)
```
{% endraw %}

**Extra Credit:**
- Add a `relationships` test to your `stg_orders` model for the customer_id in `stg_customers`
- Add tests throughout the rest of your models.
- Write your own data tests