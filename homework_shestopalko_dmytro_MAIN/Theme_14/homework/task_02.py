# Write a class structure that implements a library. Classes:
# 1) Library - name, books = [], authors = []
# 2) Book - name, year, author (author must be an instance of Author class)
# 3) Author - name, country, birthday, books = []
# Library class

# Methods:
# - new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list for the current library.
# - group_by_author(author: Author) - returns a list of all books grouped by the specified author
# - group_by_year(year: int) - returns a list of all the books grouped by the specified year
# All 3 classes must have a readable __repr__ and __str__ methods.
# Also, the book class should have a class variable which holds the amount of all existing books

class Library():
    # all_books =
    def __init__(self, books: list, authors: list):
        self.books = books
        self.authors = authors


class Author(Library):
    def __init__(self, name_auth: str, country: str, birthday: str, books: list):
        self.name_auth = name_auth
        self.country = country
        self.birthday = birthday
        self.books = books

author_001 = Author("Mark Zukerberg", "USA", "11.11.1990", "How to become a billionaire.")
print(f"Hello! I am {author_001.name_auth}. My homecountry is {author_001.country}. My birthday is on {author_001.birthday}."
      f"I wrote a book {author_001.books}")


class Book(Library):
    def __init__(self, name_book: str, year: int, author: str):
        self.name_book = name_book
        self.year = year
        self.author = Author(author)

    def new_book(self, name_book: str, year: int, author: Author):
        pass

    def group_by_author(self, author: Author):
        pass

    def group_by_year(self, year: int):
        pass





