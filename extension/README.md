# WikiTrust 2.0

## What it Does

#### This Extension Consists of:

- A content script [core/WikiTrust.js](core/WikiTrust.js) that get injected on wikipedia domains:

  This injects a button into the html of the Wikipedia page which, when pressed, adds the UI frame and runs the highlighting functionality.

#### How to Install:

- As a Firefox extension:

  1.  Visit [about:debugging](about:debugging) in the address bar and then click on This Firefox -> Load Temporary Add-On.
  2.  Select the manifest.json in this extension folder.
  3.  You should see the WikiTrust extension installed.
  4.  Go to a wiki page to test.

- As a Chrome extension:

  1.  Visit [chrome://extensions](chrome://extensions) in the address bar.
  2.  Enable Developer Options in the top right.
  3.  Cick Load Unpacked Extension.
  4.  Select the extension folder.
  5.  You should see the WikiTrust extension installed.
  6.  Go to a wiki page to test.

- As a Bookmarklet:

  **To test what the up-to-date Bookmarklet would do:** </br>
  copy-and-paste the contents of [core/WikiTrust.js](core/WikiTrust.js) into your browser's web debug console.

  _Note: This relies on the js being hosted online, so this will load an old version as a demo:_

  1. Drag and drop this link > <a href="javascript:(function(){var%20script=document.createElement('script');script.src='https://kw-m.github.io/Portfolio-Website/WikiTrust/core/WikiTrust.js';document.getElementsByTagName('head')[0].appendChild(script);script.remove()})()">WikiTrust</a> < into your browser's bookmarks bar, or long press -> save as bookmark on mobile.
  2. To use, visit a wiki page and click the bookmark, as if it was an extension. On mobile, visit a wiki and enter "WikiTrust" in the address bar, then tap the bookmark.
