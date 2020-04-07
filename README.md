

## learn.getdbt.com

Marketing website for dbt learn

Deployed with Netlify


To run locally:
1. Ensure you have ruby installed with `ruby --version`
2. Install Jekyll:
    * Run `bundle install`
    * Run `bundle exec jekyll --version` and confirm you have jekyll v3.8.x
3. Install the `www.getdbt.com` repo to get the right fonts:
    * `git submodule init`
    * `git submodule update`
4. Serve the website: `bundle exec jekyll serve --incremental --baseurl '' -w --port 5017`
5. Navigate to `http://127.0.0.1:5017/`
