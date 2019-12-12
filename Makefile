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
ext-build:
	cd C:\Program Files (x86)\Google\Chrome\Application && \
	chrome.exe --pack-extension=C:\Users\Joe\Classes\CSE115a\extension --pack-extension-key=C:\Users\Joe\Classes\CSE115a\extension.pem --no-message-box

# BACKEND
backend-setup:
	cd wikitrustbackend && \
	pip install -r requirements.txt --no-index
backend-test:
	python wikitrustbackend\FirestoreTester.py
	python wikitrustbackend\chdiff.py
	python wikitrustbackend\DiffEngine.py
	python wikitrustbackend\ReputationEngine.py
	python wikitrustbackend\WikiEngineTest.py
backend: