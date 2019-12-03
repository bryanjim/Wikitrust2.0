# Testing
How to test Wikitrust 2.0

- Look at Makefile to test certain functions
- Most python files when run have auto tests
- js can be tested through npm

Heres is an example:
```
backend-test:
	python wikitrustbackend\FirestoreTester.py
	python wikitrustbackend\chdiff.py
	python wikitrustbackend\DiffEngine.py
	python wikitrustbackend\ReputationEngine.py
```