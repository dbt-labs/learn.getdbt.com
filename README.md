

## learn.getdbt.com

The everything website for dbt Learn:
* Marketinng

This is a static site, compiled with Jekyll and deployed with Netlify.

Run with:
```
$ bundle exec jekyll serve --incremental --baseurl '' -w --port 5017
```

To run locally:
1. Ensure `jekyll` is installed with `jeykll --version` (if it's not installed, [here](https://jekyllrb.com/docs/installation/macos/) are the docs)
2. Ensure that the `www.getdbt.com` styles are available locally: `git submodule init && git submodule update`
3. `jekyll serve`
