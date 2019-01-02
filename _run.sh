# Run the site with config overrides.

# chmod u+x run.sh
#!/bin/bash
open http://localhost:5017
bundle exec jekyll serve --incremental --baseurl '' -w --port 5017
