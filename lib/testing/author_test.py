import pytest
from classes.many_to_many import Author, Magazine, Article

class TestAuthor:
    def test_author_initialization(self):
        author = Author("John Doe")
        assert author.name == "John Doe"

    def test_author_articles(self):
        author = Author("Jane Doe")
        magazine = Magazine("Health Weekly", "Health")
        article = author.add_article(magazine, "Understanding Health")
        assert author.articles() == [article]

    def test_author_magazines(self):
        author = Author("Alice Smith")
        magazine1 = Magazine("Tech Today", "Technology")
        magazine2 = Magazine("Science Monthly", "Science")
        author.add_article(magazine1, "The Future of Tech")
        author.add_article(magazine2, "Exploring Science")
        assert author.magazines() == [magazine1, magazine2]

    def test_author_topic_areas(self):
        author = Author("Bob Brown")
        magazine1 = Magazine("Health Weekly", "Health")
        magazine2 = Magazine("Tech Today", "Technology")
        author.add_article(magazine1, "Health Tips")
        author.add_article(magazine2, "Tech Innovations")
        assert author.topic_areas() == ["Health", "Technology"]
