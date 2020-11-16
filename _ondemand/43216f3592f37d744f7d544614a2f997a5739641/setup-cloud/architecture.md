---
layout: lesson
module: Set up dbt Cloud
moduleSlug: setup-cloud
title: dbt Cloud Architecture

---

# dbt Cloud Architecture
If you are new to dbt, the underlying architecture may be new to you.  First read this quick overview and then follow the steps for creating the necessary accounts.  There are effectively two ways in which to use dbt: dbt CLI and dbt Cloud.

* **dbt CLI** is a command line tool that can be run in a local environment.
* **dbt Cloud** is a hosted version that streamlines development with an online Integrated Development Environment and an interface to run dbt on a schedule.

dbt is designed to handle the transformation layer of the 'extract-load-transform' framework for data warehousing.  dbt creates a connection to a data warehouse and runs SQL code against the warehouse to transform data.  In this course, we will be using **Snowflake** as our data warehouse.

dbt also enables developers to leverage a version control system to manage their code base.  A very popular version control system is git.  If you are unfamiliar with git, don't worry, dbt Cloud provides a UI that makes it simple to use git.  When using git, we need a place to host the code base.  In this course, we will be using **GitHub** to host the code base that we build.

All in all, dbt Cloud is going to be the transformation interface between the code you write (stored and managed in GitHub) and the sample data we have to work with (stored and transformed in Snowflake).

Now let's start setting up your individual accounts.  In the following lessons, we will work to ensure all of these are connected appropriately

### dbt Cloud

If you already have a user account at cloud.getdbt.com, your instructor likely already added you to the dbt Cloud account.  When you login to dbt Cloud, you should be able to toggle into the name of your training account (e.g. Fishtown Jumpstart)

If you have not created a user account at cloud.getdbt.com, your instructor likely sent you an invitation to join the training dbt Cloud account.  This invitation will guide you through the steps for creating a dbt Cloud account.

Note: If your organization is using SSO on the multi-tenant account (cloud.getdbt.com) then your instructor likely sent an invitation to your provided personal email.  Please ensure you log out of work based dbt Cloud account before accepting the invite to ensure this account gets associated with your personal email.

### Snowflake

We have set up a Snowflake instance exclusively for training purposes.  This will be entirely separate from any warehouse your organization may be using with any real data.  Your instructor sent you personalized credentials in the welcome email.  Make sure that you login to Snowflake to change your password before proceeding with the following lessons.

### GitHub

We will be using personal GitHub accounts for saving your code throughout the course.  If you already have a GitHub account, you will be able to use this for the course.  If you don't have a GitHub account, you can make one for free at www.github.com.

Once you have finished logging in to these three accounts, you are ready to start connecting these different accounts together.