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
    def __init__(self):
        pass

class Author(Library):
    def __init__(self, name_auth: str, country: str, birthday: str, books: list):
        self.name_auth = name_auth
        self.country = country
        self.birthday = birthday
        self.books = books


class Book(Library):
    def __init__(self, name_book: str, year: int, author):
        self.name_book = name_book
        self.year = year
        self.author = Author.author

