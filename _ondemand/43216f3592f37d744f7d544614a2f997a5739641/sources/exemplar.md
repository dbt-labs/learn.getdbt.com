---
layout: lesson
module: Sources
moduleSlug: sources
title: Exemplar
---

## Exemplar

#### Self-check src_stripe and stg_payments
*Use this page to check your own work on these three models.*

**`models/staging/stripe/src_stripe.yml`**

```yml
version: 2

sources:
    - name: stripe
      database: raw
      tables:
        - name: payment
```

**`models/staging/stripe/stg_payments.sql`**

{% raw %}
```
select
    id as payment_id,
    orderid as order_id,
    paymentmethod as payment_method,
    status,

    -- amount is stored in cents, convert it to dollars
    amount / 100 as amount,
    created as created_at

from {{ source('stripe','payment') }}
```
{% endraw %}