from book import Book


class Library():
    def __init__(self):
        """Initialize the empty book list"""
        self.books = []
        pass

    def add_title(self, title, author):
        """Add a Book object with the given title and author to the book list"""
        my_book = Book(title, author)
        self.books.append(my_book)
        pass

    def count_books(self):
        """Return the number of books currently in the booklist"""
        return len(self.books)
        pass

    def remove_title(self, title):
        """Remove a book from the book list""" 
        book_indices = []
        for i in range(len(self.books)):
            current_book = self.books[i]
            if current_book.title == title:
                book_indices.append(i)
        for j in book_indices:
            self.books.pop(j)
            pass

    def is_empty(self):
        """Return True if the book list is empty, False if not"""
        return self.books == []

    def display_books(self):
        sorted_books = sorted(self.books, key=lambda i:  i.title)
        for book in sorted_books:
            print(book)
