---
layout: lesson
module: Tests
moduleSlug: tests
title: Exemplar
---

## Exemplar

Add a `relationships` test to your `stg_orders` model for the customer_id in `stg_customers`

```
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
            - relationships:
                to: ref('stg_customers')
                field: customer_id
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

