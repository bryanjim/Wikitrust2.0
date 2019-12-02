from Firestore import Firestore
from WikiEngine import WikiEngine
import ReputationEngine as re
import random as r

TRUST_REVISION_COUNT = 75

f = Firestore()
w = WikiEngine()

def start():
    articlesToComb = ["Stomach", "HIV", "Apple", "Google", "Toyota", "Disney", "Flower"]
    for article in articlesToComb:
        do(article)

def do(title):
    print("Doing " + title + "...")

    # Grab n revisions
    rev_list = w.get_revision_ids(title, TRUST_REVISION_COUNT)

    print("revs: " + str(rev_list))

    text_list = []
    auth_list = []
    for rev_id in rev_list:
        auth_list.append(r.randrange(90,100))
        text_list.append(w.get_revision_text(rev_id))

    print("Got " + str(len(text_list))+ " texts...")

    rep_arr, moves, insertions, deletes = re.getRepArray(text_list, 1, auth_list)
    trust = re.getFinalTrust(rep_arr)
    print("trust " + str(trust))

    print("Putting to db")
    print(trust)

    # Store data in db
    data = { 
        u"overall_trust": float(trust),
        u"author_trust": float(trust),
        u"moves": int(moves),
        u"insertions": int(insertions),
        u"deletes": int(deletes)
    }

    #print(data)
    f.writeData(title, data)

    # # make sure it stored
    print(f.readData(title))

start()