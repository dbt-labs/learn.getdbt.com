---
layout: lesson
module: Sources
moduleSlug: sources
---

# Practice 
Using the resources in this module, complete the following in your dbt project:

**Configure Sources:**
- Configure a source for the tables `raw.jaffle_shop.customers` and `raw.jaffle_shop.orders` in a file called `src_jaffle_shop.yml`
- Configure a source for the tables `raw.stripe.payment` in a file called `src_stripe.yml`

**Refactor Staging Models:**
- Refactor `stg_customers` using the source macro.
- Refactor `stg_orders` using the source macro.
- Refactor `stg_payments` using the source macro.

**Add Documentation and Tests:**
- Add documentation at the model and table level of your tables
- Add `unique` and `not_null` tests to the ID's in each of your sources

**Review Documentation:**
- Generate documentation to view the sources in your DAG

**Extra Credit:**
- Configure your Stripe payments data to check for source freshness.
- Run snapshot-freshness.