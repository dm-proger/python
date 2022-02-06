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

    def group_by_author(self, author: Author):
        if not isinstance(author, Author):
            raise TypeError("There is no such author")
        try:
            new_book = list(filter(lambda book: book.author == author, self.books))
            if not new_book:
                print(f"No books found for author {author.name_auth}")
            else:
                print(new_book)
                return new_book
        except TypeError as exc:
            print(exc)


    def group_by_year(self, year: int):
        new_book = list(filter(lambda book: book.year == year, self.books))
        if new_book == []:
            print(f"No books found by year {year}")
        else:
            print(new_book)
            return new_book


def main():
    author_001 = Author("Mark Zukerberg", "USA", "11.11.1990")
    author_002 = Author("Tim Cook", "USA", "12.12.1991")
    author_003 = Author("John Kennedy", "USA", "10.10.1991")
    # print(f"Hello! I am {author_001.name_auth}. My homecountry is {author_001.country}. My birthday is on {author_001.birthday}."
    #       f"I wrote a book {author_001.books}")

    library_01 = Library("Central Library")
    library_01.new_book("Name of a new book_01", 2020, author_001)
    library_01.new_book("Name of a new book_0101", 2020, author_001)
    library_01.new_book("Second name of a book", 2021, author_002)
    library_01.new_book("Third name of a book", 2020, author_003)

    print(library_01.group_by_author(author_001))
    # print(library_01.books, library_01.authors)

if __name__ == "__main__":
    main()







