---
layout: lesson
module: Jinja Primer
moduleSlug: jinja-primer
title: Review
render_with_liquid: false
---

# Review

**Jinja** is a templating language written in the python programming language.  Jinja is used in dbt to write functional SQL.  For example, we can write a dynamic pivot model using Jinja.

**Jinja Basics**

The best place to learn about leveraging Jinja is the [template designer documentation](https://jinja.palletsprojects.com/en/2.11.x/templates/).

There are three Jinja delimiters to be aware of in Jinja.

- `{% … %}` is used for statements.  There perform any function programming such as setting a variable or starting a for loop.
- `{{ … }}` is used for expressions.  These will print text to the rendered file.  In most cases in dbt, this will compile your Jinja to pure SQL.
- `{# … #}` is used for comments.  This allows us to document our code inline.  This will not be rendered in the pure Jinja that you write to th

A few helpful features of Jinja include dictionaries, lists, if/else statements, for loops, and macros.

**Dictionaries** are data structures composed of key-value pairs.
```
{% set person = {
    ‘name’: ‘me’,
    ‘number’: 3
} %}

{{ person.name }}

me

{{ person[‘number’] }}

3
```
**Lists** are data structures that are ordered and indexed by integers.
```
{% set self = [‘me’, ‘myself’] %}

{{ self[0] }}

me
```
**If/else statements** are control statements that make it possible to provide instructions for a computer to make decisions based on clear criteria.
```
{% set temperature = 80% %}

On a day like this, I especially like

{% if temperature >70 %}

a refreshing mango sorbet.

{% else %}

A decadent chocolate ice cream.

{% endif %}

On a day like this, I especially like

a refreshing mango sorbet
```
**For loops** make it possible to repeat a code block while passing different values for each iteration through the loop.
```
{% set flavors = [‘chocolate’, ‘vanilla’, ‘strawberry’] %}

{% for flavor in flavors %}

Today I want {{ flavor }} ice cream!

{% endfor %}

Today I want chocolate ice cream!

Today I want vanilla ice cream!

Today I want strawberry ice cream!
```
**Macros** are a way of writing functions in Jinja.  This allows us to write a set of statements once and then reference those statements throughout your code base.
```
{% macro hoyquiero(flavor, dessert = ‘ice cream’) %}

Today I want {{ flavor }} {{ dessert }}!

{% endmacro %}

{{ hoyquiero(flavor = ‘chocolate’) }}

Today I want chocolate ice cream!

{{ hoyquiero(mango, sorbet) }}

Today I want mango sorbet!
```
**Whitespace Control**

We can control for whitespace by adding a single dash on either side of the Jinja delimiter.  This will trim the whitespace between the Jinja delimiter on that side of the expression.

**Bringing it all Together!**

We saw that we could refactor the following pivot model in pure SQL using Jinja to make it more dynamic to pivot on a list of payment mentors.

**Original SQL:**
```
with payments as (
   select * from {{ ref('stg_payments') }}
),
 
final as (
   select
       order_id,
 
       sum(case when payment_method = 'bank_transfer' then amount else 0 end) as bank_transfer_amount,
       sum(case when payment_method = 'credit_card' then amount else 0 end) as credit_card_amount,
       sum(case when payment_method = 'coupon' then amount else 0 end) as coupon_amount,
       sum(case when payment_method = 'gift_card' then amount else 0 end) as gift_card_amount
 
   from {{ ref('stg_payments') }}
 
   group by 1
)
 
select * from final
```

**Refactored Jinja + SQL:**
```
{%- set payment_methods = ['bank_transfer','credit_card','coupon','gift_card'] -%}
 
with payments as (
   select * from {{ ref('stg_payments') }}
),
 
final as (
   select
       order_id,
       {% for payment_method in payment_methods -%}
 
       sum(case when payment_method = '{{ payment_method }}' then amount else 0 end) 
            as {{ payment_method }}_amount
          
       {%- if not loop.last -%}
         ,
       {% endif -%}
 
       {%- endfor %}
   from {{ ref('stg_payments') }}
   group by 1
)
 
select * from final
```
