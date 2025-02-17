class Book:
    def __init__(self, title, author):
        self.title: str = title
        self.author: str = author
        self.available: bool = True
        self.borrower: str | None = None
        self._validate_data()  # Validate data at creation

    def get_info(self):
        """Возвращает информацию о книге."""
        return f"{self.title} by {self.author}"

    def change_status(self, status, borrower=None):
        """
        Изменяет статус доступности книги и записывает заемщика, если книга берется.
        Если возвращается книга (status=True), заемщик сбрасывается.
        """
        if self.available == status:
            return "Статус уже установлен."
        if status:  # возвращаем книгу
            self.available = True
            self.borrower = None  # всегда сбрасываем заемщика при возврате
            return "Книга теперь доступна."
        else:  # выдаем книгу
            if not borrower:
                return "Ошибка: необходимо указать заемщика."
            self.available = False
            self.borrower = borrower
            return f"Книга взята {borrower}."

    def _validate_data(self):
        """Protected: Проверяет корректность данных книги."""
        if not self.title or not self.author:
            raise ValueError("Название и автор книги должны быть указаны!")
