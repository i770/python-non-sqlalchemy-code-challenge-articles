import pytest
from classes.many_to_many import Magazine, Author, Article

class TestMagazine:
    def test_magazine_initialization(self):
        magazine = Magazine("Tech Today", "Technology")
        assert magazine.name == "Tech Today"
        assert magazine.category == "Technology"

    def test_magazine_articles(self):
        magazine = Magazine("Health Weekly", "Health")
        author = Author("Jane Doe")
        article = author.add_article(magazine, "Health Tips")
        assert magazine.articles() == [article]

    def test_magazine_contributors(self):
        magazine = Magazine("Science Monthly", "Science")
        author1 = Author("Alice Smith")
        author2 = Author("Bob Brown")
        author1.add_article(magazine, "Exploring Science")
        author2.add_article(magazine, "Science Innovations")
        assert magazine.contributors() == [author1, author2]

    def test_magazine_article_titles(self):
        magazine = Magazine("Tech Today", "Technology")
        author = Author("John Doe")
        author.add_article(magazine, "The Future of Tech")
        assert magazine.article_titles() == ["The Future of Tech"]

    def test_magazine_contributing_authors(self):
        magazine = Magazine("Health Weekly", "Health")
        author1 = Author("Jane Doe")
        author2 = Author("John Smith")
        author3 = Author("Alice Johnson")
        author1.add_article(magazine, "Health Tips")
        author2.add_article(magazine, "Healthy Living")
        author3.add_article(magazine, "Nutrition 101")
        assert magazine.contributing_authors() == [author1, author2, author3]
