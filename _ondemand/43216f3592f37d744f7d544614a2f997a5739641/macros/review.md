---
layout: lesson
module: Macros
moduleSlug: macros
title: Review
render_with_liquid: false
---

# Review

**Macros** are functions that are written in Jinja.  This allows us to write generic logic once, and then reference that logic throughout our project.  

Consider the case where we have three models that use the same logic.  We could copy paste the logic between those three models.  If we want to change that logic, we need to make the change in three different places.

Macros allow us to write that logic once in one place and then reference that logic in those three models.  If we want to change the logic, we make that change in the definition of the macro and this is automatically used in those three models.  

**DRY Code**

Macros allow us to write DRY (Don’t Repeat Yourself) code in our dbt project.  This allows us to take one model file that was 200 lines of code and compress it down to 50 lines of code.  We can do this by abstracting away the logic into macros.

**Tradeoff**

As you work through your dbt project, it is important to balance the readability/maintainability of your code with how concise your code (or DRY) your code is.  Always remember that you are not the only one using this code, so be mindful and intentional about where you use macros.

**Macro Example: Cents to Dollars**

**Original Model:**
```
select
  id as payment_id,
  orderid as order_id,
  paymentmethod as payment_method,
  status,

  -- amount stored in cents, convert to dollars
  amount / 100 as amount,
  created as created_at

from {{ source(‘stripe’, ‘payment’) }}
```
**New Macro:**
```
{% macro cents_to_dollars(column_name, decimal_places=2) -%}
round( 1.0 * {{ column_name }} / 100, {{ decimal_places }})
{%- endmacro %}
```
**Refactored Model:**
```
select
  id as payment_id,
  orderid as order_id,
  paymentmethod as payment_method,
  status,

  -- amount stored in cents, convert to dollars
  {{ cents_to_dollars(‘payment_amount’) }} as amount
  created as created_at

from {{ source(‘stripe’, ‘payment’) }}
```