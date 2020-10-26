---
layout: lesson
module: Docs
moduleSlug: docs
title: Practice
---

# Practice 
Using the resources in this module, complete the following in your dbt project:

**Write Documentation:**
- Add documentation to the file `models/staging/jaffle_shop/stg_jaffle_shop.yml`
- Add a description for your `stg_customers` model and the column `customer_id`
- Add a description for your `stg_orders` model and the column `order_id`

**`models/staging/jaffle_shop/stg_jaffle_shop.yml`**
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

**Create a Reference a Doc Block:**
- Create a doc block for your `stg_orders` model to document the `status` column.
- Reference this doc block in the description of `status` in `stg_orders`  (see this in the code snippet above)

**`models/staging/jaffle_shop/jaffle_shop.md`**

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

**Generate and view documentation:**
- Generate the documentation
- View the documentation that you wrote for the `stg_orders` model.
- View the DAG for your project

**Extra Credit:**
- Add documentation to the other columns in `stg_customers` and `stg_orders`
- Add documentation to the `stg_payments` model.
- Create a doc block for another place in your project and generate this in your documentation.
