

## learn.getdbt.com

Marketing website for dbt learn

Deployed with netlify

Run with:
```
$ bundle exec jekyll serve --incremental --baseurl '' -w --port 5017
```

To regenerate the tutorial:
1. Go to your cloned repo, make sure you're on the `learn` branch
2. `npm run build`
3. Go to this repo, `cd` into `_site`
4. `bash deploy.sh`
5. `jekyll serve -o` and then go to `/tutorial/setting-up`