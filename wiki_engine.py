import requests
import pprint
from bs4 import BeautifulSoup
import difflib

def get_revision_ids(page):
    PARAMS = {
        "action": "query",
        "titles": [page],
        "prop": "revisions",
        "rvlimit": 2,
        #"rvprop": "content",
        #"rvslots":"main",
        "format": "json"
    }
    url = "https://en.wikipedia.org/w/api.php"
    request = requests.get(url=url, params=PARAMS)
    data = request.json()
    revision_list = []
    pageid = list(data["query"]["pages"].keys())[0]
    for x in data["query"]["pages"][pageid]["revisions"]:
        revision_list.append(x["revid"])
    return revision_list

def get_revision_text(revision_id):
    PARAMS = {
        "action": "parse",
        "oldid": revision_id,
        "format": "json"
    }
    url = "https://en.wikipedia.org/w/api.php"
    r = requests.get(url=url, params=PARAMS)
    data = r.json()
    soup = BeautifulSoup(data["parse"]["text"]["*"], 'lxml')
    paragraphs = soup.find_all('p')
    revision_string = ""
    for p in paragraphs:
        revision_string += p.text
    return revision_string

def diff_revisions(page):
    '''
    Args:
    page: this is the title of the page to get diff revisions.

    Returns:
    A list of revisions text.
    '''

    revid_list = get_revision_ids(page)
    revisions = [get_revision_text(revid) for revid in revid_list]

    return revisions