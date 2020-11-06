---
layout: lesson
module: Sources
moduleSlug: sources
title: Test and Document
---

{% include options/ondemand/wistia_embed.html %}

#### Reference: Code Snippets

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
              description: Primary key for customers.
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

**Generate Documentation**

Run `dbt docs generate` from the command line