# Legacy learn.getdbt.com

**This repository no longer powers learn.getdbt.com.** The index page of learn.getdbt.com, and most subpages, will now redirect you to www.getdbt.com/dbt-learn. 

This repository remains mostly to serve the `_redirects` file and act as a code reference. 

You can now reach the /lessons files directly at https://www.getdbt.com/dbt-learn/lessons/.

Since the redirects file is not processed in the local dev environment, you may still run the legacy site locally. See instructions below.

## Getting Started

**To run locally:**
1. Ensure `jekyll` is installed with `jekyll --version` (if it's not installed, [here](https://jekyllrb.com/docs/installation/macos/) are the docs)
2. Ensure that the `www.getdbt.com` styles are available locally: `git submodule init && git submodule update`
3. `jekyll serve`

## Remark.js
* Currently used for dbt Learn distributed.
* Presentations are located in `_lessons`
* Use `presentation` as your layout in the front matter of your presentation html file.
* Adjust the styling using in `_config/_includes/options/styles-learn.html`
