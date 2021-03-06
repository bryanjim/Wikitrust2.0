# Wikitrust2.0

First, we must talk about Wikitrust 1.0:

WikiTrust is a software product, available as a Firefox Plugin, which aimed to assist editors in detecting vandalism and dubious edits, by highlighting the "untrustworthy" text with a yellow or orange background. As of September 2017, the server is offline, but the code is still available for download, and parts of the code are being updated.

- Between 4% and 6% of Wikipedia edits are considered vandalism  
- Colorcode the risky edits. Text from questionable sources starts out with a bright orange background, while text from trusted authors gets a lighter shade.
- WikiTrust assigns a reputation score to every word in every article.
- Fundamentally depends on the concept of Darwinian natural selection. The longer information persists on the page, the more accurate it's likely to be.
- Based on an person’s past contributions, WikiTrust computes a reputation score between zero and nine. 


The WikiTrust 2.0 project aims at compute a reputation value for Wikipedia text that indicates how well the text has been revised.  This index of text reputation can be used to spot new, and as yet unrevised, contributions, and it can also be used to automatically select a good-quality, recent revision for a Wikipedia page.

We want to build a new version of WikiTrust, geared initially at examining:
- Pages of political candidates in elections
- Pages related to medicine and pharmaceutical dosages
- Pages that are considered top importance

# Structure

```
root
  donecritera/     : Our definiton of Done
  extension/       : Source code for our ext
  releaseplan/     : Current & Future release
  sprints/         : Sprint plans, reports, burnups
  wikitrustbackend : The crux, all the algos + DB
  wikitrustweb     : Old web app
 ...
```

# Frontend

## Chrome Extension

To install:

- As a Chrome extension:

  1.  Visit [chrome://extensions](chrome://extensions) in the address bar.
  2.  Enable Developer Options in the top right.
  3.  Cick Load Unpacked Extension.
  4.  Select the extension folder.
  5.  You should see the WikiTrust extension installed.

## ~~Web App~~ DEPRICATED

We no longer will develop this, please check our chrome Extension

### Available Scripts

In the project directory, you can run:

#### `npm start`

Runs the app in the development mode.<br />
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.


### `npm test`

Launches the test runner in the interactive watch mode.<br />
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.<br />
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.<br />
Your app is ready to be deployed!

# Core Algorithm

The Algorithm of the software consists of 3 main parts:

**chdiff**

This function computes the list of edits that converts one version of the article to another.
In general, when this functin presented with the input of two strings, it return an array of edits.
This information is later used by the other two main components of the backend.

**author_reputation**

This file contains the necessary classes that are used to compute the author reputation. The authorEngine can be executed in order to test the computation of the author reputation values. To do this, a string array of versions should be passed into createRepArray() function. Then, getAuthorReputation(repArray) function should be called. This function will create an array and compute all the reputations of authors edited each version. getFinalRepVal() function will then return a float values that is the author reputation of the final version's author to be displayed.

**text_reputation**

This file contains the necessary classes that are used to compute the text reputation. The ReputationEngine can be executed in order to test the computation of the author reputation values. The values calculated by author_reputation should be passed to this engine. Than, a string array of versions should be passed into getRepArray()function. This function will create an array and compute all the reputations of each words within each version. The function getOverallTrust(i) will return the overall trust value of ith function. Similarly, the function getFinalTrust() will return the final reputation value to be displayed.

# Infastructure

We use a FirestoreDB to store our data and a simple NodeJS layer to serve as an api

# Testing

Tests can be found in Testing.md

# Authors
Joseph Csoti, Cagan Bakirci, Bryan Jimenez

# Thanks

Prof. Luca De Alfaro  
Wikimedia Foundation


#### Last updated Dec 02 2019