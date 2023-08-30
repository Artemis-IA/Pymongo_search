from pymongo import MongoClient

class DBManager:
    def __init__(self, db_url, db_name, collection_name):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def get_publications(self, offset, per_page):
        return self.collection.find().skip(offset).limit(per_page)

    def get_authors(self):
        return self.collection.distinct('authors')

    def get_publications_by_author(self, author):
        return self.collection.find({'authors': author})

    def get_publications_by_date(self, start_date):
        return self.collection.find({'year': {'$gte': start_date}})

    def get_publication_by_id(self, publication_id):
        return self.collection.find_one({'_id': publication_id})

    def add_publication(self, data):
        return self.collection.insert_one(data)

    def get_publication_count(self):
        return self.collection.count_documents({})

    def close_connection(self):
        self.client.close()
