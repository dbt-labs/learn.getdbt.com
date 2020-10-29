---
layout: lesson
module: Analyses and Seeds
moduleSlug: analyses-seeds
title: Practice
---

## Practice

#### Analyses
Using you new knowledge of analyses, create an analysis file in the `analyses` folder called `total_revenue.sql` that uses the `stg_payments` model and sums the amount of successful payments.  (Remember to use Jinja in this rather than the raw table name)

#### Seeds
Using your new knowledge of seeds, create a seed file in the `data` folder called `employees.csv` with the following values:

```
employee_id, email, customer_id
3425, mike@jaffleshop.com, 1
2354, sarah@jaffleshop.com, 6
2342, frank@jaffleshop.com, 8
1234, jennifer@jaffleshop.com, 9
```

Build this seed into your data warehouse by running `dbt seed`.