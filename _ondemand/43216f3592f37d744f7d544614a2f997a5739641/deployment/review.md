---
layout: lesson
module: Deployment
moduleSlug: deployment
---

# Review

### Development vs. Deployment
* Development in dbt is the process of building, refactoring, and organizing different files in your dbt project.  This is done in a development environment using a development schema (`dbt_jsmith`) and typically on a *non-default* branch (i.e. master, main).
* Deployment in dbt (or running dbt in production) is the process of running dbt on a schedule in a deployment environment.  The deployment environment will typically run from the *default* branch and use a decleared deployment schema (`dbt_prod`).
* These use of multiple environments makes is possible to continue to building your dbt project without breaking the production models that power the rest of your organization.

### Creating your Deployment Environment
* A deployment environmnet can be configured in dbt Cloud on the Environments page.
* **General Settings** You can configure which dbt version you want to use and specify a branch other than the default branch.
* **Data Warehouse Connection** You can set data warehouse specific configurations here.  For example, you may choose to use a dedicated warehouse for your production runs in Snowflake.
* **Deployment Credentials** Here is where you enter the credential dbt will use to access your Data Warehouse:
  * IMPORTANT: You should set up a **separate Data Warehouse** account for this run.  This should not be the same account that you personally use in development.  (This was done in the demo for simplicity)
  * IMPORTANT: Your schema in production should be **different** from anyone's development schema.

### Scheduling a job in dbt Cloud
* Scheduling of future jobs can be configured in dbt Cloud on the Jobs page.
* You can select the deployment environment that you created before or a different environment if needed.
* **Commands** A single job can run multiple dbt commands.  For example, you can run `dbt run` and `dbt test` back to back on a schedule.  You don't need to configure these as separate jobs.
* **Triggers** This section is where the schedule can be set for the particular job.
* After a job has been created, you can manually start the job by selecting `Run Now`

### Reviewing Cloud Jobs
* The results of a particular job run can be reviewed as the job completes and over time.
* The logs for each command can be reviewed.
* If documentation was generated, this can be viewed.
* If `dbt source snapshot-freshness` was run, this can also be viewed at the end of a job.