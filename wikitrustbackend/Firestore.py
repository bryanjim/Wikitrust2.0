from google.cloud import firestore

class Firestore:
    def __init__(self):
        self.db = firestore.Client()
        self.DB_COLLECTION_ARTICLES = self.db.collection(u"articles")

    def writeData(self, id, data):
        diff_ref = self.DB_COLLECTION_ARTICLES.document(id)
        diff_ref.set(data)

    def readData(self, id):
        diff_ref = self.DB_COLLECTION_ARTICLES.document(id)

        try:
            data = diff_ref.get()
            return data.to_dict()
        except Exception as e:
            return "ERROR: " + e