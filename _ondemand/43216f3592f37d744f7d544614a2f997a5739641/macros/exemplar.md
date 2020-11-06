---
layout: lesson
module: Macros
moduleSlug: macros
title: Practice
---

## Exemplar

`macros/cents_to_dollars.sql`

{% raw %}
```
{% macro cents_to_dollars(column_name, decimal_places=2) -%}
    round( 1.0 * {{ column_name }} / 100, {{ decimal_places }})
{%- endmacro %}
```
{% endraw %}


Refactored `stg_payments.sql`

{% raw %}
```
select
    id as payment_id,
    orderid as order_id,
    paymentmethod as payment_method,
    status,

    -- amount is stored in cents, convert it to dollars
    {{ cents_to_dollars('amount', 4) }} as amount,
    created as created_at

from {{ source('stripe','payment') }}
```
{% endraw %}