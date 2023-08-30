from models import Publication, Author

class PublicationManager:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def get_publication_details(self, publication_id):
        data = self.db_manager.get_publication_by_id(publication_id)
        return Publication(data)

    def add_publication(self, data):
        self.db_manager.add_publication(data)

class AuthorManager:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def get_authors(self):
        return [Author(name) for name in self.db_manager.get_authors()]