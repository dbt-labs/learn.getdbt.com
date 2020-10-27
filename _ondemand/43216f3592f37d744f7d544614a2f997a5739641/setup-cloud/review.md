---
layout: lesson
module: Set up dbt Cloud
moduleSlug: setup-cloud
title: Review

---

# Review

#### GitHub Repository and Connection

After you have created a dbt Cloud account, it can be helpful to create an empty repository and grant dbt Cloud access to this repository.

**Create an empty repository over in GitHub**
* Make sure this a completely empty repository.  Do not create a `.gitignore` or `README.md` yet.  
* This will allow dbt Cloud to initialize your dbt project.

**Grant access for dbt Cloud to connect to GitHub**
* Choose your profile in the top right of dbt Cloud.
* Navigate to integration.
* Configure the GitHub configuration.
* Grant specific access to the repository you just created.

#### Connecting to your Warehouse and Repository
When setting up your project, you will need to make a connection to your **warehouse** and **repository**.

**Create a new project**
* Choose the hamburger menu in the top left and choose account settings.
* Select new project.  This starts the new project workflow.

**Connect to your warehouse**
* Read the [dbt docs](https://docs.getdbt.com/docs/dbt-cloud/cloud-configuring-dbt-cloud/connecting-your-database) for your respective warehouse to connect to your warehouse.
* Decide on a development schema.  We recommend something like this `dbt_jsmith`.  This is the schema that dbt will write to while you are developing.
* Choose 'Test' to ensure that the connection works.

**Connect to your repository**
* You already gave dbt Cloud access to your empty repository.
* Choose to connect to a GitHub repository - not a Managed repository.
* You should be able to select the new empty repository.

**Initialize your Project**
* Navigate to the develop interface.
* You should see the green button 'Initialize Project' - click this.
* This will run `dbt init` which will set up the file system for your dbt project.

#### Cloud IDE
A quick tour of the Cloud IDE.  The IDE can be found by choosing the hamburger menu in the top left and choosing 'Develop'.

<img src="/ui/img/ondemand/cloud_ide.png" style="width: 80%;">

**File Tree**
* This is the main view into your dbt project.
* This is where a dbt project is built in the form or .sql, .yml, and other file types.

**Text Editor**
* This is where individual files are edited.  Different files can be selected from the file tree to the left.
* This supports multiple tabs to toggle between files.
* Statement tabs are simply worksheets that can be used to run SQL against your Data Warehouse.  These are not associated with a particular file.

**Compile SQL / Run SQL**
* These two buttons apply to statements and SQL files.
* `Compile SQL` will compile any Jinja to render Pure SQL.  This will be displayed in the Info Window in Compiled SQL.
* `Run SQL` will compile and run your query against the data warehouse as a simple query.  The results will be displayed in the Info Window in Results.

**Command Line**
* This is where you can execute specific dbt commands (e.g. `dbt run`, `dbt test`).
* This will pop up to show the results as they are processed.  Logs can also be viewed here.

**Info Window**
* This window will show results when choosing Compile SQL and Run SQL.
* This is helpful for troubleshooting errors during development. 

**Git Controls**
* All git commands in the IDE are completed here.
* This will change dynamically based on the git status of your project.

**View Docs**
* This button will display the documentation for your dbt project.
* More details on this in the documentation module.