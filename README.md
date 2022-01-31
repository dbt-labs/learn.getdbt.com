# Legacy learn.getdbt.com

**This repository no longer powers learn.getdbt.com.** The index page of learn.getdbt.com, and most subpages, will now redirect you to www.getdbt.com/dbt-learn. 

This repository remains mostly to serve the `_redirects` file and act as a code reference. 

*Notable exception:* **the /lessons directory, which is used for teaching trainings, is not being redirected**. If you need to make changes to the training slides, you will still do it here.

You can reach the /lessons files directly at learn.getdbt.com/lessons, or, in the preview environment, at https://deploy-preview-XXX--kind-lovelace-c014dc.netlify.app/lessons, where "XXX" is the pull request number. 

Since the redirects file is not processed in the local dev environment, you may still run the legacy site locally. See instructions below.

## Getting Started

**To run locally:**
1. Ensure `jekyll` is installed with `jeykll --version` (if it's not installed, [here](https://jekyllrb.com/docs/installation/macos/) are the docs)
2. Ensure that the `www.getdbt.com` styles are available locally: `git submodule init && git submodule update`
3. `jekyll serve`

## Remark.js
* Currently used for dbt Learn distributed.
* Presentations are located in `_lessons`
* Use `presentation` as your layout in the front matter of your presentation html file.
* Adjust the styling using in `_config/_includes/options/styles-learn.html`

## Reveal.js
* Exploring using this for dbt Learn on demand
* Presentations are located in `_ondemand`
* Use `reveal` as your layout in the front matter of your presentation html file.
* Adjust the styling using .scss in `stylesheets/styles-ondemand.scss` or create your own.
