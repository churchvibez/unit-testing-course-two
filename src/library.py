import json
from src.book import Book
from src.member import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def _levenshtein_distance(self, s1: str, s2: str):
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                cost = 0 if s1[i - 1] == s2[j - 1] else 1
                dp[i][j] = min(
                    dp[i - 1][j] + 1,    # удаление
                    dp[i][j - 1] + 1,    # вставка
                    dp[i - 1][j - 1] + cost  # замена
                )
        return dp[m][n]

    def add_book(self, book: Book):
        for b in self.books:
            if b.title.lower() == book.title.lower():
                return f"Книга '{book.title}' уже существует в библиотеке."
        self.books.append(book)
        return f"Книга '{book.title}' добавлена в библиотеку."

    def remove_book(self, title: str):
        """
        Удаляет книгу из библиотеки по названию.
        Независимо от текущего статуса, книга удаляется, 
        а также удаляется из списка заимствованных книг у всех членов.
        """
        book = self.find_book(title)
        if book:
            # Mark the book as unavailable and clear the borrower.
            book.available = False
            book.borrower = None
            # Remove the book from any member's borrowed_books list.
            for member in self.members:
                if book in member.borrowed_books:
                    member.borrowed_books.remove(book)
            # Remove the book from the library's list.
            self.books.remove(book)
            return f"Книга '{title}' удалена из библиотеки."
        return "Книга не найдена."


    def add_member(self, member: Member):
        for m in self.members:
            if m.name.lower() == member.name.lower():
                return f"Пользователь '{member.name}' уже существует."
        self.members.append(member)
        return f"Пользователь '{member.name}' добавлен в библиотеку."

    def _find_book(self, title: str):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        suggestions = self.suggest_books(title)
        if suggestions:
            return suggestions
        return None

    def find_book(self, title: str):
        """Public метод для поиска книги."""
        return self._find_book(title)

    def _find_member(self, name: str):
        for member in self.members:
            if member.name.lower() == name.lower():
                return member
        return None

    def suggest_books(self, title: str) -> list:
        suggestions = []
        if not title:
            return suggestions
        for book in self.books:
            distance = self._levenshtein_distance(title.lower(), book.title.lower())
            if distance < 6:
                suggestions.append(book)
        return suggestions

    def save_to_file(self, filepath: str):
        data = {
            "books": [
                {
                    "title": book.title,
                    "author": book.author,
                    "available": book.available,
                    "borrower": book.borrower,
                }
                for book in self.books
            ],
            "members": [
                {
                    "name": member.name,
                    "borrowed_books": [book.title for book in member.borrowed_books],
                }
                for member in self.members
            ],
        }
        try:
            with open(filepath, "w") as file:
                json.dump(data, file, indent=4)
            return f"Информация сохранена в файл: {filepath}."
        except Exception as e:
            return f"Ошибка сохранения: {str(e)}"

    def load_from_file(self, filepath: str):
        try:
            with open(filepath, "r") as file:
                data = json.load(file)
        except Exception as e:
            return f"Ошибка загрузки: {str(e)}"

        self.books = [Book(book["title"], book["author"]) for book in data.get("books", [])]
        for book, book_data in zip(self.books, data.get("books", [])):
            book.available = book_data.get("available", True)
            book.borrower = book_data.get("borrower")
        self.members = [Member(member["name"]) for member in data.get("members", [])]
        for member, member_data in zip(self.members, data.get("members", [])):
            member.borrowed_books = [self.find_book(title) for title in member_data.get("borrowed_books", [])]
        return f"Информация загружена из: {filepath}."
