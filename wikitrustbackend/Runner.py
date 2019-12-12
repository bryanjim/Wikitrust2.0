# This file contains the code for the runner of the WikiTrust
# algorithm. This file connects all the individual parts
# in the project.
#
# Joseph Csoti, November 2019
# Cagan Bakirci, November 2019


from Firestore import Firestore
from WikiEngine import WikiEngine
import ReputationEngine as re
import authorEngine as ae
import random as r

TRUST_REVISION_COUNT = 75

f = Firestore()
w = WikiEngine()

def start():
    # what articles to crawl
    articlesToComb = [
        "Stomach", 
        "HIV", 
        "Apple", 
        "Google", 
        "Toyota", 
        "Disney", 
        "Flower",
        "The Art of War",
        "Code of Hammurabi",
        "Euclid's Elements",
        "Eugene Onegin",
        "Hamlet",
        "Republic",
        "The Prince",
        "One Thousand and One Nights",
        "Dream of the Red Chamber",
        "Don Quixote",
        "The Lord of the Rings",
        "The Tale of Genji",
        "Epic of Gilgamesh",
        "Iliad",
        "Journey to the West",
        "Odyssey",
        "Parzival",
        "Romance of the Three Kingdoms",
        "Water Margin",
        "Dead Sea Scrolls",
        "Encyclopædia Britannica",
        "On the Origin of Species",
        "Oxford English Dictionary",
        "Gulliver's Travels",
        "King Lear",
        "Macbeth",
        "A Midsummer Night's Dream",
        "Romeo and Juliet",
        "Alice's Adventures in Wonderland",
        "The Brothers Karamazov",
        "The Catcher in the Rye"
]
    for article in articlesToComb:
        do(article)

def do(title):
    print("Doing " + title + "...")

    # Grab n revision ids
    rev_list = w.get_revision_ids(title, TRUST_REVISION_COUNT)

    print("revs: " + str(rev_list))

    text_list = []
    auth_list = []
    # grab texts
    for rev_id in rev_list:
        auth_list.append(r.randrange(90,100))
        text_list.append(w.get_revision_text(rev_id))

    print("xxxx", auth_list)

    print("Got " + str(len(text_list))+ " texts...")

    # get rep + edit numbers
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

    # Write to db
    f.writeData(title, data)

    # Read from db
    print(f.readData(title))

start()