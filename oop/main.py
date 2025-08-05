from library_system import Book, EBook, PrintBook, Library

def main():
    library = Library()
    library.add_book(Book("Pride and Prejudice", "Jane Austen"))
    library.add_book(EBook("Snow Crash", "Neal Stephenson", "500KB"))
    library.add_book(PrintBook("The Catcher in the Rye", "J.D. Salinger", 234))
    
    library.display_books()

if __name__ == "__main__":
    main()
