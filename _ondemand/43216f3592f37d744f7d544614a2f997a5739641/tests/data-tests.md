---
layout: lesson
module: Tests
moduleSlug: tests
title: Data Tests

---

{% include options/ondemand/wistia_embed.html %}

#### Reference: Code Snippets

**tests/assert_positive_total_for_payments.sql**

*Note how this is a .sql file in the tests directory*
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