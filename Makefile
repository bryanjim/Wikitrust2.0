# WEB
web-setup:
	cd wikitrustweb && \
	npm install

web-test:
	cd wikitrustweb && \
	npm test

web-build:
	cd wikitrustweb && \
	npm run build

# EXTENSION
ext-setup:
ext-test:
ext:

# BACKEND
backend-setup:
	cd wikitrustbackend && \
	pip install -r requirements.txt --no-index
backend-test:
	python wikitrustbackend\FirestoreTester.py
backend: