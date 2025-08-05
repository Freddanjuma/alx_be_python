# Base class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        return f"Book: {self.title} by {self.author}"


# Derived class 1: EBook
class EBook(Book):
    def __init__(self, title, author, file_size_kb):
        super().__init__(title, author)
        self.file_size_kb = file_size_kb

    def get_info(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size_kb}KB"


# Derived class 2: PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def get_info(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Composition: Library has a collection of books
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Only Book objects can be added.")

    def list_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                print(book.get_info())
