---
layout: lesson
module: Models
moduleSlug: models
---

# Practice 
Using the resources in this module, complete the following in your dbt project:

**Quick Project Polishing:**
- In your `dbt_project.yml` file, change the name of your project from `my_new_project` to `jaffle_shop` (line 5 AND 35)

**Staging Models:**
- Create a `staging` directory in your models file
- Create a `stg_customers` model for `raw.jaffle_shop.customers`

```sql
select
    id as customer_id,
    first_name,
    last_name

from raw.jaffle_shop.customers
```

- Create a `stg_orders` model for `raw.jaffle_shop.orders`

```sql
select
    id as order_id,
    user_id as customer_id,
    order_date,
    status

from raw.jaffle_shop.orders
```

**Mart Models:**
- Create a `marts` directory in your models file
- Create a `dim_customers` model

**Configure your materializations:**
- In your `dbt_project.yml` file, configure the staging directory to be materialized as views.

```yml
models:
  jaffle_shop:
    staging:
      +materialized: view
```

- In your `dbt_project.yml` file, configure the models directory to be materialized as views.

```yml
models:
  jaffle_shop:
  ...
    marts:
      +materialized: table
```

**Building an Orders Model:**
- Use the statement tab or Snowflake to inspect `raw.stripe.payment`
- Create a `stg_payments` model.
- Create a `orders` model with the following fields
    - order_id
    - customer_id
    - amount (hint: this has to come from payments)

**Refactor your Customers Model:**
- Add a new field to the customers model:
    - `customers.lifetime_value`: the total amount a customer has spent at `jaffle_shop`
    - Hint: The sum of lifetime_value is $1,672
