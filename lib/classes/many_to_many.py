class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if hasattr(self, "title"):
            pass
        elif isinstance(title, str) and (5 <= len(title) <= 50):
            self._title = title
        else:
            raise Exception("title must be a string between 5 and 50 characters")
        
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception("author must be an instance of the Author class")
        
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise Exception("author must be an instance of the Author class")
        
class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if hasattr(self, "name"):
            pass
        elif isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise Exception("name must be a string with length > 0")

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        categories = list(set([magazine.category for magazine in self.magazines()]))

        return categories if len(categories) > 0 else None

class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and (2 <= len(name) <= 16):
            self._name = name
        else:
            raise Exception("name must be a string between 2 and 16 characters")
        
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise Exception("category must be a string with length > 0")

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors_w_duplicates(self):
        return [article.author for article in self.articles()]
    
    def contributors(self):
        return list(set(self.contributors_w_duplicates()))

    def article_titles(self):
        titles = [article.title for article in self.articles()]

        return titles if len(titles) > 0 else None

    def contributing_authors(self):
        author_list = self.contributors_w_duplicates()
        contr_authors = list(set([author for author in author_list if author_list.count(author) > 1]))
        
        return contr_authors if len(contr_authors) > 0 else None
    
    @classmethod
    def top_publisher(cls):
        top_mag = None
        top_count = 0

        for magazine in cls.all:
            article_count = len(magazine.articles())
            
            if article_count > top_count:
                top_count = article_count
                top_mag = magazine

        return top_mag