---
layout: lesson
module: Tests
moduleSlug: tests
title: Data Tests

---

{% include options/ondemand/wistia_embed.html %}

*Note: The file structure in this video does not map to previous videos OR your current project.  Check out the Practice page for clarification for how to add this to you project.*

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

**dbt Commands**
- Execute `dbt test` to run all **schema** and **data** tests in your project.
- Execute `dbt test --date` to run only **data tests** in your project.
