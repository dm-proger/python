# Write a class structure that implements a library. Classes:
# 1) Library - name, books = [], authors = []
# 2) Book - name, year, author (author must be an instance of Author class)
# 3) Author - name, country, birthday, books = []

# All 3 classes must have a readable __repr__ and __str__ methods.


class Author():
    def __init__(self, name_auth: str, country: str, birthday: str, books: list =[]):
        self.name_auth = name_auth
        self.country = country
        self.birthday = birthday
        self.books = books

    def __repr__(self):
        return self.name_auth

class Book():
    books_list = []

    def __init__(self, name_book: str, year: int, author: Author):
        self.name_book = name_book
        self.year = year
        self.author = author

    def __repr__(self):
        return f"{self.name_book}, {self.year}"

class Library():
    def __init__(self, library_name: str, books: list = [], authors: list = []):
        self.library_name = library_name
        self.books = books
        self.authors = authors

    def __repr__(self):
        return self.books


    def new_book(self, book_name: str, book_year: int, author:Author):
        book_01 = Book(name_book=book_name, year=book_year, author=author)
        self.books.append(book_01)
        self.authors.append(author)
        author.books.append(book_01)

    # - group_by_author(author: Author) - returns a list of all books grouped by the specified author
    def group_by_author(self, author: Author):
        pass

    # - group_by_year(year: int) - returns a list of all the books grouped by the specified year
    def group_by_year(self, year: int):
        pass


def main():
    author_001 = Author("Mark Zukerberg", "USA", "11.11.1990")
    print(f"Hello! I am {author_001.name_auth}. My homecountry is {author_001.country}. My birthday is on {author_001.birthday}."
          f"I wrote a book {author_001.books}")

    library_01 = Library("Name of the library")
    library_01.new_book("Name of a new book", 2020, author_001)
    print(library_01.books, library_01.authors)

if __name__ == "__main__":
    main()







