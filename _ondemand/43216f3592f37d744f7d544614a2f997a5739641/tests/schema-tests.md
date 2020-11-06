---
layout: lesson
module: Tests
moduleSlug: tests
title: Schema Tests
---

{% include options/ondemand/wistia_embed.html %}

#### Reference: Code Snippets

**models/staging/jaffle_shop/stg_jaffle_shop.yml**

*Note how this is a .yml file rather than a .sql file*

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
        - name: status
          tests:
            - accepted_values:
                values:
                  - completed
                  - shipped
                  - returned
                  - placed
```

