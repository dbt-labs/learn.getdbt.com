---
layout: lesson
module: Sources
moduleSlug: sources
title: Source Freshness
---

{% include options/ondemand/wistia_embed.html %}

#### Reference: Code Snippets

**models/staging/jaffle_shop/src_jaffle_shop**

*Note: The descriptions and tests have been dropped to make this code snippet more concise.*

{% raw %}
```
version: 2

sources:
    - name: jaffle_shop
      database: raw
      tables:
        - name: customers
          columns:
            - name: id
              
        - name: orders
          loaded_at_field: _etl_loaded_at
          freshness:
            warn_after: {count: 12, period: hour}
            error_after: {count: 24, period: hour}
          columns:
            - name: id
```
{% endraw %}