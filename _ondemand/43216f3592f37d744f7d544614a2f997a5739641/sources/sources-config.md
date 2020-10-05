---
layout: lesson
module: Sources
moduleSlug: sources
title: Configure Sources
---

{% include options/ondemand/wistia_embed.html %}

#### Reference: Code Snippets

**models/staging/jaffle_shop/src_jaffle_shop**

```yml
version: 2

sources:
    - name: jaffle_shop
      database: raw
      tables:
        - name: customers
        - name: orders
```

**models/staging/jaffle_shop/stg_customers**

{% raw %}
```
select 
    id from customer_id,
    first_name,
    last_name
from {{ source('jaffle_shop','customers') }}
```
{% endraw %}

**models/staging/jaffle_shop/stg_orders**

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