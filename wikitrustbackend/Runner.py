from Firestore import Firestore
from WikiEngine import WikiEngine
import DiffEngine, ReputationEngine

f = Firestore()
w = WikiEngine()

def start():
    articlesToComb = ["HIV", "Stomach", "Apple", "WikiTrust", "Google"]
    for article in articlesToComb:
        do(article, 0, 1)

def do(title, a, b):
    print("Doing " + title + " -- VER " + str(a) + " vs. " + str(b))
    rev_list = w.get_revision_ids(title, 5) # no change

    ver_a = rev_list[a]
    ver_b = rev_list[b]

    rev_a = w.get_revision_text(ver_a)
    rev_b = w.get_revision_text(ver_b)

    articleToWrite = {u"title": str(title), u"text": rev_a, u"diff": ""}
    f.writeArticle(str(ver_a), articleToWrite)

    # Compute diff
    diff = DiffEngine.compute_edit_list(rev_a, rev_b)

    # Compute rep from diff
    parsed_diff = ReputationEngine.parseArray(str(diff))
    rep = ReputationEngine.assignTrust(parsed_diff)

    print("Reputation: " + str(rep))

    # Store data in db
    id = str(rev_list[0]) + '.' + str(rev_list[1])
    data = {u"diff_moves": str(diff), u"diff_trust": [1, 2, 3, 4], u"trust": rep}
    f.writeDiff(id, data)

    # make sure it stored
    print(f.readDiff(id))



start()