# Book Library Management Project

class Book:

    def __init__(self, book_id, title, author, is_borrowed=False):
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

    @property
    def show_borrowed_books(self):
        return [book for book in self.books.values() if book.is_borrowed]

    def borrow_book(self, book_id):
        if book_id in self.books and not self.books[book_id].is_borrowed:
            self.books[book_id].is_borrowed = True
            print(f"\nBook with ID {book_id} is borrowed")
        else:
            print(f"\n[!] Book with ID {book_id} is not available")


class ChildLibrary(Library):
    def __init__(self):
        super().__init__()
        self.child_books = {}  # {1: True, 2: False}

    def add_book(self, book, for_child):
        super().add_book(book)
        self.child_books[book.book_id] = for_child

    def borrow_book(self, book_id):
        if book_id in self.books and not self.books[book_id].is_borrowed:
            if self.child_books[book_id]:
                print(f"\n[!] Book with ID {book_id} is for children only")
            else:
                self.books[book_id].is_borrowed = True
                print(f"\nBook with ID {book_id} is borrowed")
        else:
            print(f"\n[!] Book with ID {book_id} is not available")


if __name__ == '__main__':
    library = ChildLibrary()

    book = Book(1, "Python", "Guido van Rossum")
    book2 = Book(2, "Java", "James Gosling")
    book3 = Book(3, "Learn to Color", "John Doe")

    # print(book)
    # print(book2)

    library.add_book(book, for_child=False)
    library.add_book(book2, for_child=False)
    library.add_book(book3, for_child=True)

    print(f"\nBook in Library: {library.show_books}")

    library.borrow_book(1)
    library.borrow_book(2)
    library.borrow_book(1)

    print(f"\nBooks in Library: {library.show_books}")

    print(f"\nBorrowed Books: {library.show_borrowed_books}")

    print(f"\nBooks for Children: {library.child_books}")
