from Firestore import Firestore
import random as r

# Create object
f = Firestore()

def genRandData():
    return {
        u'author_trust': round(r.uniform(0.0, 100.0),2),
        u'deletes': r.randrange(0,100),
        u'insertions': r.randrange(0,100),
        u'moves': r.randrange(0,100),
        u'overall_trust': round(r.uniform(0.0, 100.0),2)
    }

def writeTest(id, data):
    f.writeData(id, data)
    return f.readData(id) == data

def readTest(id, data):
    return f.readData(id) == data

def deleteTest(id):
    f.deleteData(id)
    return True

if __name__ == "__main__":
    teststorun = 25
    testspassed = 0
    wfail = 0
    rfail = 0
    dfail = 0
    for i in range(0,teststorun):

        id = r.randrange(11111,99999)
        obj = genRandData()

        wtest = writeTest(str(id), obj)
        rtest = readTest(str(id), obj)
        dtest = deleteTest(str(id))


        passedAll = writeTest and rtest and dtest

        if passedAll: testspassed += 1

        if not wtest: wfail +=1
        if not rtest: rfail +=1
        if not dtest: dfail +=1

        msg = "PASSED" if passedAll else "FAILED"
        print("Test #" + str(i) + ": " + msg)

    print("All tests done -- " + str(testspassed) + "/" + str(teststorun) + " PASSED")
    print(str(wfail) + " write failures")
    print(str(rfail) + " read failures")
    print(str(dfail) + " delete failures")