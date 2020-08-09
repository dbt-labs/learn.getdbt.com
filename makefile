
run:
	git submodule update
	echo "Open localhost:5017 in your browser"
	bundle exec jekyll serve --baseurl '' -w --port 5017

build:
	git submodule update
	bundle update
	jekyll build --baseurl ''
