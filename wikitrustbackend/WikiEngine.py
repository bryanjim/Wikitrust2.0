import requests
import pprint
from bs4 import BeautifulSoup
import difflib
import re

class WikiEngine:

    url = "https://en.wikipedia.org/w/api.php"
    
    def diff_revisions(self, page):
        '''
        Args:
        page: this is the title of the page to get diff revisions.

        Returns:
        A list of revisions text.
        '''

        revid_list = self.get_revision_ids(page, 2)
        revisions = [self.get_revision_text(revid) for revid in revid_list]

        return revisions
    
    def get_revision_ids(self, page, limit):
        PARAMS = {
            "action": "query",
            "titles": [page],
            "prop": "revisions",
            "rvlimit": limit,
            #"rvprop": "content",
            #"rvslots":"main",
            "format": "json"
        }
        request = requests.get(url=self.url, params=PARAMS)
        data = request.json()
        revision_list = []
        pageid = list(data["query"]["pages"].keys())[0]
        for x in data["query"]["pages"][pageid]["revisions"]:
            revision_list.append(x["revid"])
        return revision_list

    def get_revision_text(self,revision_id):
        PARAMS = {
            "action": "parse",
            "oldid": revision_id,
            "format": "json"
        }
        r = requests.get(url=self.url, params=PARAMS)
        data = r.json()
        soup = BeautifulSoup(data["parse"]["text"]["*"], 'lxml')
        paragraphs = soup.find_all('p')
        revision_string = ""
        for p in paragraphs:
            revision_string += p.text
        return revision_string