---
layout: overview
title: Group assignment
---

# How to work through this assignment

To get the most value out of this assignment, we recommend that you try to work through each problem as follows:
* First, attempt to complete the exercise by using [docs.getdbt.com](https://docs.getdbt.com/). Learning how to read docs is a skill that will serve you well as you continue to use dbt!
* Check the related [lesson slides](https://learn.getdbt.com/lessons) for relevant code snippets.
* If you hit errors, check out the docs on [debugging](https://docs.getdbt.com/docs/guides/debugging-errors/) for tips.

Then, try using the resources available to you during dbt Learn, including:
* Ask someone in your breakout group (including your tutor)
* Ask in our shared Slack channel

If you get _really_ stuck, we do have worked solutions. Use these as a last resort — writing code that doesn't work is part of the learning experience!
* Each exercise maps to a separate pull request [here](https://github.com/fishtown-analytics/dbt-learn-demo-v2/pulls?q=is%3Apr+is%3Amerged+). You can use to see how we completed this exercise. Remember that the code is only half of the exercise, you should also be comfortable running the related dbt commands.
* If you get yourself into an absolute tangle, consider forking the above [demo repo](https://github.com/fishtown-analytics/dbt-learn-demo-v2/) to get back on track.

---

# Common pitfalls

1. Forgetting to `save` a file before running it. We've _all_ been there. Over time it becomes muscle memory. A dot next to a filename indicates that a file isn't saved.
2. dbt Cloud users: Hitting the `run` button, rather than executing `dbt run` in the terminal prompt
    * The `run sql` button executes whatever SQL statement is on your screen
    * The `dbt run` command builds relations in your database
<center>
<img src="/ui/img{{page.id}}/run-sql-vs-dbt-run.png" style="width: 80%;">
</center>

---

# Prerequisites

Before going further, make sure:
1. You have completed the [pre-work](https://docs.getdbt.com/learn/setting-up/)
2. You have added an `orders` model to your project (from [this morning's session](dbt-fundamentals#working-session))
3. Your project is in a repository owned by your personal GitHub account, and is set to public
4. You can run `dbt run` and `dbt test` without any errors

If you need any help with these, please let us know.

---

# Follow a git flow
For each exercise, we recommend you follow a git flow.
1. Checkout a new branch¹:
    - **dbt CLI:** In the terminal: `git checkout -b name-of-exercise`
    - **dbt Cloud:** Click the `create a new branch` button (see below)
2. Make your changes, ensure they work, and then commit your changes¹
3. Open up a pull request²
    - Navigate to your repository in GitHub
    - Click the "New pull request" button
4. [Bonus] Assign it to a classmate to review:
    - You will need to add your classmate as a [collaborator](https://docs.github.com/en/github-ae@latest/github/setting-up-and-managing-your-github-user-account/inviting-collaborators-to-a-personal-repository)
<center>
<img src="/ui/img{{page.id}}/create-new-branch.png" style="width: 50%;">
</center>

¹Stuck on what to name your branch or what a good commit message it? We've got a [guide for that](https://github.com/fishtown-analytics/corp/blob/master/git-guide.md)!
²Check out our tips on good pull requests [here](pull-requests)

---

### 1. Add more tests to your project

* Ensure that your `orders` model has at least one test on it (and it passes)

#### Related resources:
* [docs.getdbt.com](https://docs.getdbt.com/docs/testing#section-schema-tests)

### 2. Add sources to your project
* Add `sources` for our two data sources: `jaffle_shop` and `stripe`
* Update your `raw.<schema>.<table>` references in your models with {% raw %}`{{ source() }}`{% endraw %} functions
* Add a freshness block to at least one source (find a table that has a column that indicates when the row was loaded), and snapshot the freshness
* Add tests to these sources, and try running these tests

#### Related resources:
* [docs.getdbt.com](https://docs.getdbt.com/docs/using-sources)

### 3. Add documentation to your project
* Add a description for one (or all!) of the following:
    * a model
    * a source
    * a column
* Use a docs block for one of your descriptions
* Generate and view the documentation website

#### Related resources
* [docs.getdbt.com](https://docs.getdbt.com/docs/documentation)

---

# Additional exercises
If you get through the above exercises, feel free to keep going with these 👇

### Refactor your project
Based on our discussion in [Designing a dbt project](dbt-project-design), refactor your project to be consistent with how we (Fishtown) structure our dbt projects. Consider
* model naming
* organization within directories

#### Related resources:
* [Discourse article on structuring projects](https://discourse.getdbt.com/t/how-we-structure-our-dbt-projects/355)


### Set up your dbt project to run on a schedule and in CI
* Create a deployment environment (related [tutorial](https://docs.getdbt.com/tutorial/deploy-your-project/))
* Create a job that runs on a schedule
* Set up continuous integration for the job (related [docs](https://docs.getdbt.com/tutorial/deploy-your-project/))

### Polish your project
* Skip ahead to tomorrow's lesson on [polishing a dbt project](polish-project), and try implementing some of these recommendations in your own project!
* If you just implemented CI, confirm that you get a ✅ on your PR before merging it

### Ask for a tutor review!
* If you've finished this assignment and want some feedback on code style, ask your tutor to review your work.
* Or, if you're already using dbt, use this time to get some feedback on your company's dbt project.
