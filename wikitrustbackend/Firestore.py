from google.cloud import firestore


class Firestore:
    def __init__(self):
        self.db = firestore.Client()
        self.DB_COLLECTION_DIFFS = self.db.collection(u"diffs")
        self.DB_COLLECTION_ARTICLES = self.db.collection(u"articles")

    def writeDiff(self, id, data):
        diff_ref = self.DB_COLLECTION_DIFFS.document(id)
        diff_ref.set(data)

    def readDiff(self, id):
        diff_ref = self.DB_COLLECTION_DIFFS.document(id)

        try:
            data = diff_ref.get()
            return data.to_dict()
        except Exception as e:
            return "ERROR: " + e

    def writeArticle(self, id, data):
        diff_ref = self.DB_COLLECTION_ARTICLES.document(id)
        diff_ref.set(data)

    def readArticle(self, id):
        article_ref = self.DB_COLLECTION_ARTICLES.document(id)

        try:
            data = article_ref.get()
            return data.to_dict()
        except Exception as e:
            return "ERROR: " + e

