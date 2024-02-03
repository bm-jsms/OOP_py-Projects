# Book Library Management Project

class Book:

    def __init__(self, book_id, title, author, is_borrowed):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"\nBook ID: {self.book_id} \nTitle: {self.title} \nAuthor: {self.author} \nBorrowed: {self.is_borrowed}"

    def __repr__(self):
        return self.__str__()


class Library:

    def __init__(self):
        self.books = {}  # {1: Book {1, "Python", "Guido van Rossum", False}, 2: Book {2, "Java", "James Gosling", True}

    def add_book(self, book):
        if book.book_id not in self.books:
            self.books[book.book_id] = book
        else:
            print(f"Book with ID {book.book_id} already exists")

    def remove_book(self, book):
        self.books.remove(book)

    @property
    def show_books(self):
        return [book for book in self.books.values() if not book.is_borrowed]


if __name__ == '__main__':
    library = Library()

    book = Book(1, "Python", "Guido van Rossum", False)
    book2 = Book(2, "Java", "James Gosling", True)

    # print(book)
    # print(book2)

    library.add_book(book)
    library.add_book(book2)

    print(library.show_books)
