from Firestore import Firestore
import random as r

# Create object
f = Firestore()

def genRandData(obj):
    return {
        u'author_trust': round(r.uniform(0.0, 100.0),2),
        u'deletes': r.randrange(0,100),
        u'insertions': r.randrange(0,100),
        u'moves': r.randrange(0,100),
        u'overall_trust': round(r.uniform(0.0, 100.0),2)
    }

def writeTest(id, data):
    # print("Writing to " + str(id) + "...")
    f.writeData(id, data)

def readTest(id):
    # print("Reading from " + str(id) + "...")
    print(f.readData(id))

def deleteTest(id):
    # print("Deleting " + str(id) + "...")
    f.deleteData(id)

if __name__ == "__main__":
    for i in range(0,5):
        id = r.randrange(11111,99999)
        obj = {}
        writeTest(str(id), genRandData(obj))
        readTest(str(id))
        deleteTest(str(id))
        print("Test #" + str(i) + ": PASSED")
    print("All tests PASSED")