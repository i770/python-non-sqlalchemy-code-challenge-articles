import pytest
from classes.many_to_many import Article, Magazine, Author

class TestArticle:
    def test_article_initialization(self):
        author = Author("John Doe")
        magazine = Magazine("Tech Today", "Technology")
        article = Article(author, magazine, "The Future of Tech")
        
        assert article.author == author
        assert article.magazine == magazine
        assert article.title == "The Future of Tech"

    def test_article_title_validation(self):
        author = Author("Jane Doe")
        magazine = Magazine("Health Weekly", "Health")
        with pytest.raises(ValueError):
            Article(author, magazine, "Hi")  # Title too short

    def test_article_association(self):
        author = Author("Alice Smith")
        magazine = Magazine("Science Monthly", "Science")
        article = Article(author, magazine, "Exploring the Universe")
        
        assert author.articles() == [article]
        assert magazine.articles() == [article]
