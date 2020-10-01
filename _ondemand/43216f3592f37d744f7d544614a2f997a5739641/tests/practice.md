---
layout: lesson
module: Tests
moduleSlug: tests
title: Practice
---

# Practice 
Using the resources in this module, complete the following in your dbt project:

**Schema Tests:**
- Add tests to your jaffle_shop staging tables:
    - Create a file called `stg_jaffle_shop.yml` for congfiguring your tests
    - Add `unique` and `not_null` tests to the keys for each of your staging tables
    - Add an `accepted_values` test to your `stg_orders` model for status.
    - Add a `relationships` test to your `stg_orders` model for the customer_id in `stg_customers`
    - Run your tests

**Data Tests:**
- Add the test `assert_positive_value_for_total_amount` to be run on your `stg_payments` model.
- Run your tests

**Extra Credit:**
- Add tests throughout the rest of your models.
- Write your own data tests