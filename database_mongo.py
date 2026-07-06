class MockCollection:
    def __init__(self):
        self.data = []
        self.counter = 1

    def insert_one(self, doc):
        doc["_id"] = str(self.counter)
        self.counter += 1
        self.data.append(doc)

    def find(self, query):
        results = []
        for doc in self.data:
            match = True
            for k, v in query.items():
                if doc.get(k) != v:
                    match = False
                    break
            if match:
                results.append(doc.copy())
        return results

    def update_one(self, query, update):
        for doc in self.data:
            if doc.get("_id") == query.get("_id"):
                for k, v in update.get("$set", {}).items():
                    doc[k] = v

    def delete_one(self, query):
        self.data = [doc for doc in self.data if doc.get("_id") != query.get("_id")]


activity_logs_collection = MockCollection()
notifications_collection = MockCollection()
comments_collection = MockCollection()
