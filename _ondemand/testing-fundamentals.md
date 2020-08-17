---
layout: overview
title: Testing Fundamentals
learningObjectives:
  - Explain the role of testing in software engineering
  - Explain the role of testing in analytics engineering
  - Explain the two types of tests in dbt.
  - Name the four fundamental tests in dbt
  - Configure tests in your dbt project
  - Execute all or a subset of tests in your dbt project
  - Interpret the results of a test in dbt.
---

# Why is Testing important?
_Why is testing relevent for your organization?_
<iframe width="560" height="315" src="https://www.youtube.com/embed/9JUz16BrQrY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# Learning Objectives
{% for objective in page.learningObjectives %}
   <li> {{ objective }} </li>
{% endfor %}


# What exactly is Testing?
_How can we borrow software engineering principles and apply them to analytics?_
<iframe src="https://fast.wistia.net/embed/iframe/paz9tohikt" title="What is Testing? Video" allow="autoplay; fullscreen" allowtransparency="true" frameborder="0" scrolling="no" class="wistia_embed" name="wistia_embed" allowfullscreen msallowfullscreen width="560" height="315"></iframe>
<script src="https://fast.wistia.net/assets/external/E-v1.js" async></script>

# Testing in dbt
_How do we implement testing in dbt?_
<iframe src="https://player.vimeo.com/video/446933852" width="560" height="315" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>

# Review

* **Testing** is used in software engineering to make sure that the code does what we expect it to.
* In Analytics Engineering, testing allows us to make sure that the transformations we write SQL for produce a model that meets our assertions.
* In dbt, tests are written as select statements.  These select statements are run against your materialized models to ensure they meet your assertions.
* In dbt, there are two types of tests - schema tests and data tests:
  * **Schema tests** are applied in YAML and return the number of records that do not meet your assertions.  These are run on specific columns in a model.
  * **Data tests** are specific queries that you run against your models.  A data test passes if the number of records returned is 0.  These are run on the entire model.
* dbt ships with four built in tests - unique, not null, accepted values, relationships
  * **Unique** tests to see if every value in a column is unique
  * **Not_null** tests to see if every value in a column is something other than null
  * **Accepted_values** tests to make sure every value in a column is equal to a value in a provided list.
  * **Relationships** test ensures that every value in the current model exists in another model. (see: referential integrity
* Schema tests are configured in a YAML file where as data tests are stored as select statements in the tests folder.
* Tests can be run against your current project using a range of commands:
  * `dbt test`    runs all tests in the dbt project 
  * `dbt test --data`
  * `dbt test --schema`
  * `dbt test -models one_specific_model`
* Read more here in [docs](https://docs.getdbt.com/reference/commands/test)
* In development, dbt Cloud will provide a visual for the results of your tests.  Each test produces a log that the users can investigate the results of the test further.

<img src="/ui/img{{page.id}}/testing-dev.png" style="width: 100%;">

* In production, dbt Cloud can be scheduled to run `dbt test`.  The ‘Run History’ tab provides a similar interface for viewing the test results.

<img src="/ui/img{{page.id}}/testing-prod.png" style="width: 100%;">
