---
layout: lesson
module: Documentation
moduleSlug: docs
---

# Review

**Documentation**
* Documentation is essential for an analytics team to work effectively and efficiently.  Strong documentations empowers the ability to self-service questions about data and for new team members to on-board.
* Often documentation lags behind the coding it is meant to describe.  This tends to happen because documenting is a separate process from the coding itself.
* Due to this, documentation should be as automated as possible and happen as close as possible to the coding.
* In dbt, models are built in SQL files and these same models are documented in the same models directory in YML files.

**Writing Documentation and Doc Blocks**
* Documentation of models occurs in the YML files (with testing) inside the models directory.  It is helpful to store this alongside the subfolder related models.
* For models, descriptions can happen on the model level or at the column level.
* If a longer form, more styled version of text would provide a strong description, **doc blocks** can be used to render markdown in the generated documentation.

**Generating and Viewing Documentation**
* In the developer console, an updated version can be generated through the command `dbt docs generate`.  This will refresh the link in the top left corner of the Cloud IDE.
* The generated documentation included the following:
    * Project Level DAG
    * Model Descriptions
    * Schema Tests run on Models
    * Jinja-SQL and Compile SQL
    * and more...