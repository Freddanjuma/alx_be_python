class Book:
    def __init__(self, title, author, year):
        """Constructor: Called when a new Book object is created."""
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """User-friendly string representation of the object."""
        return f"{self.title} by {self.author} ({self.year})"

    def __repr__(self):
        """Developer-friendly string representation of the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """Destructor: Called when the Book object is deleted."""
        pass  # Destructors are rarely used for print statements in production

# Example usage
if __name__ == "__main__":
    my_book = Book("1984", "George Orwell", 1949)
    print(my_book)         # Calls __str__
    print(repr(my_book))   # Calls __repr__
