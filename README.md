# learn.getdbt.com

The everything site for dbt Learn including:
* Information about dbt Learn distributed/IRL
* dbt Learn presentations
* (Coming Soon) Landing page for dbt Learn on demand

## Getting Started


**Run with:**
```
$ bundle exec jekyll serve --incremental --baseurl '' -w --port 5017
```

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
