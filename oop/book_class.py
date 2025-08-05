class Book:
    def __init__(self, title, author, publication_year):
        """Constructor: Called when a new Book object is created."""
        self.title = title
        self.author = author
        self.publication_year = publication_year
        print(f"Book created: {self.title} by {self.author} ({self.publication_year})")

    def __str__(self):
        """User-friendly string representation of the object."""
        return f"{self.title} by {self.author} ({self.publication_year})"

    def __repr__(self):
        """Developer-friendly string representation of the object."""
        return f"Book('{self.title}', '{self.author}', {self.publication_year})"

    def __del__(self):
        """Destructor: Called when the Book object is deleted."""
        print(f"Book deleted: {self.title} by {self.author}")

# Example usage
if __name__ == "__main__":
    my_book = Book("1984", "George Orwell", 1949)
    print(my_book)         # __str__ is called here
    print(repr(my_book))   # __repr__ is called here

    # Deleting the book to trigger __del__
    del my_book
