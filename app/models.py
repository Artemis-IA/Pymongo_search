class Publication:
    def __init__(self, data):
        self.data = data

    @property
    def title(self):
        return self.data['title']

    @property
    def authors(self):
        return self.data['authors']

    @property
    def year(self):
        return self.data['year']

    @property
    def booktitle(self):
        return self.data['booktitle']

    @property
    def url(self):
        return self.data['url']

class Author:
    def __init__(self, name):
        self.name = name