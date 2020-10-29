---
layout: lesson
module: Analyses and Seeds
moduleSlug: analyses-seeds
title: Practice
---

## Exemplar

`analysis/total_revenue.sql`

```
with payments as (
    select * from {{ ref('stg_payments') }}
), 

aggregated as (
    select 
        sum(amount) as total_revenue
    from payments
    where status = 'success'
)

select * from aggregated
```

`data/employees.csv`

```
employee_id, email, customer_id
3425, mike@jaffleshop.com, 1
2354, sarah@jaffleshop.com, 6
2342, frank@jaffleshop.com, 8
1234, jennifer@jaffleshop.com, 9
```