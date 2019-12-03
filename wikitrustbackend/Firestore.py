from google.cloud import firestore

class Firestore:
    def __init__(self):
        self.db = firestore.Client()
        self.DB_COLLECTION_ARTICLES = self.db.collection(u"articles")

    def writeData(self, id, data):
        diff_ref = self.DB_COLLECTION_ARTICLES.document(id)
        diff_ref.set(data)
        # print("Wrote " + str(data) + " to " + str(id))

    def readData(self, id):
        diff_ref = self.DB_COLLECTION_ARTICLES.document(id)
        # print("Got data from " + str(id))
        try:
            data = diff_ref.get()
            return data.to_dict()
        except Exception as e:
            return "ERROR: " + e

    def deleteData(self, id):
        diff_ref = self.DB_COLLECTION_ARTICLES.document(id)
        diff_ref.delete()
        # print("Deleted data at " + str(id))