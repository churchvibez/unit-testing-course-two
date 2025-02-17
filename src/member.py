from src.book import Book

class Member:
    def __init__(self, name):
        self.name: str = name
        self.borrowed_books: list[Book] = []
        self._validate_data()  # Validate member data at creation

    def borrow_book(self, book: Book):
        """
        Adds the book to the user's borrowed list if available and under borrowing limit.
        
        Added conditionals:
         - Prevents borrowing the same book twice.
         - Enforces a borrowing limit (e.g., maximum 3 books).
         - Checks if the book is available.
        """
        if book in self.borrowed_books:
            return f"Книга '{book.title}' уже взята {self.name}."
        if len(self.borrowed_books) >= 3:
            return "Достигнут лимит заимствованных книг."
        if not book.available:
            return "Книга недоступна."

        self.borrowed_books.append(book)
        return book.change_status(False, self.name)

    def return_book(self, book: Book):
        """
        Returns the book by removing it from the borrowed list.
        
        Added conditionals:
         - Checks if the book is actually borrowed by the member.
         - Checks if the book is already marked as available.
        """
        if book not in self.borrowed_books:
            return "Этот человек не брал заданную книгу."
        self.borrowed_books.remove(book)
        if book.available:
            return f"Книга '{book.title}' уже доступна."
        return book.change_status(True)

    def _validate_data(self):
        """Protected: Validates the member's data."""
        if not self.name:
            raise ValueError("Имя пользователя должно быть указано!")
