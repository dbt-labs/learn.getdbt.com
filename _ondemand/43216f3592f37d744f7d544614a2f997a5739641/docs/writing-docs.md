---
layout: lesson
module: Documentation
moduleSlug: docs
title: Writing Documentation
---

{% include options/ondemand/wistia_embed.html %}

#### Reference: Code Snippets

*Note: The `schema.yml` file in the video has a lot more tests configure than needed to demonstrate this point.  Before you start coding this yourself, check out the practice lesson towards the end of this module for more clarification for how to add this to your project.*


**schema.yml**
{% raw %}
```
version: 2

models:

    - name: stg_customers
      description: Staged customer data from our jaffle shop app.
      columns: 
        - name: customer_id
          description: The primary key for customers.
          tests:
            - unique
            - not_null

    - name: stg_orders
      description: Staged order data from our jaffle shop app.
      columns: 
        - name: order_id
          description: Primary key for orders.
          tests:
            - unique
            - not_null
        - name: status
          description: '{{ doc("order_status") }}'
          tests:
            - accepted_values:
                values:
                  - completed
                  - shipped
                  - returned
                  - placed
```
{% endraw %}

**jaffle_shop.md**



{% raw %}
```
{% docs order_status %}

One of the following values: 

| status         | definition                                                 |
|----------------|------------------------------------------------------------|
| placed         | Order placed but not yet shipped                           |
| shipped        | Order has been shipped but hasn't yet been delivered       |
| completed      | Order has been received by customers                       |
| return_pending | Customer has indicated they would like to return this item |
| returned       | Item has been returned                                     |

{% enddocs %}
```
{% endraw %}