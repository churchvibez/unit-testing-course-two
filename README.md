# Library System Documentation

This document explains the design of the library system, including the classes and tests.

---

## Class: Book

### Description

The **Book** class represents a book in the library system. It stores and processes information about the book's title, author, availability, and current borrower.

### Attributes

- **title** (string): The title of the book.
- **author** (string): The author of the book.
- **available** (boolean): The availability status of the book. `True` if available, otherwise `False`.
- **borrower** (string or `None`): The current borrower's name if checked out; otherwise, `None`.

### Methods

- **`__init__(self, title, author)`**  
  Initializes a new book with the given title and author.  
  **Parameters:**  
  - `title` (string): The title of the book.  
  - `author` (string): The author of the book.

- **`get_info(self)`**  
  Returns a string with the book's title and author.  
  **Returns:**  
  - (string): For example, `"1984 by George Orwell"`.

- **`change_status(self, status, borrower=None)`**  
  Updates the book's availability and sets the borrower if needed.  
  **Parameters:**  
  - `status` (boolean): The new availability status.  
  - `borrower` (string, optional): The name of the borrower if the book becomes unavailable.  
  **Returns:**  
  - (string): A message indicating that the status has been changed.

- **`_validate_data(self)`** *(Protected)*  
  Checks if the book data is valid.  
  **Exceptions:**  
  - Raises `ValueError` if the title or author is missing.

---

## Class: Member

### Description

The **Member** class represents a library user who can borrow books. It holds information about the user's name and the list of borrowed books.

### Attributes

- **name** (string): The name of the library user.
- **borrowed_books** (list of Book objects): The books the member has borrowed.

### Methods

- **`__init__(self, name)`**  
  Initializes a member with the provided name.  
  **Parameters:**  
  - `name` (string): The name of the user.

- **`borrow_book(self, book)`**  
  Adds a book to the user's borrowed list if it is available.  
  **Parameters:**  
  - `book` (Book object): The book the user wishes to borrow.  
  **Returns:**  
  - (string): A message indicating whether the book was successfully borrowed or if it is unavailable.

- **`return_book(self, book)`**  
  Returns a borrowed book by removing it from the list.  
  **Parameters:**  
  - `book` (Book object): The book to return.  
  **Returns:**  
  - (string): A message indicating that the book was returned or that it was not borrowed.

- **`_validate_data(self)`** *(Protected)*  
  Validates the member's data.  
  **Exceptions:**  
  - Raises `ValueError` if the name is missing.

---

## Class: Library

### Description

The **Library** class manages books and members. It allows you to add/remove books, register members, and save/load library data from a JSON file.

### Attributes

- **books** (list): All books in the library.
- **members** (list): All library members.

### Methods

- **`__init__(self)`**  
  Initializes the library with empty lists for books and members.

- **`add_book(self, book)`**  
  Adds a book to the library.  
  **Parameters:**  
  - `book` (Book object): The book to add.  
  **Returns:**  
  - (string): A confirmation message.

- **`remove_book(self, title)`**  
  Removes a book from the library by its title. The book becomes unavailable and its borrower is reset.  
  **Parameters:**  
  - `title` (string): The title of the book to remove.  
  **Returns:**  
  - (string): A message indicating the result.

- **`add_member(self, member)`**  
  Registers a new member.  
  **Parameters:**  
  - `member` (Member object): The member to add.  
  **Returns:**  
  - (string): A confirmation message.

- **`_find_book(self, title)`** *(Protected)*  
  Searches for a book by title.  
  **Parameters:**  
  - `title` (string): The title to search for.  
  **Returns:**  
  - (Book object, list of Book objects, or `None`): The found book, a list of similar books, or `None`.

- **`_find_member(self, name)`** *(Protected)*  
  Searches for a member by name.  
  **Parameters:**  
  - `name` (string): The member's name.  
  **Returns:**  
  - (Member object or `None`): The found member or `None`.

- **`save_to_file(self, filepath)`**  
  Saves the library data (books and members) to a JSON file.  
  **Parameters:**  
  - `filepath` (string): The file path for saving data.  
  **Returns:**  
  - (string): A message indicating successful save.

- **`load_from_file(self, filepath)`**  
  Loads the library data from a JSON file.  
  **Parameters:**  
  - `filepath` (string): The file path to load data from.  
  **Returns:**  
  - (string): A message indicating successful load.

- **`_levenshtein_distance(self, s1, s2)`**  
  Calculates the Levenshtein distance between two strings.  
  **Parameters:**  
  - `s1` (string): The first string.  
  - `s2` (string): The second string.  
  **Returns:**  
  - (number): The Levenshtein distance.

- **`suggest_books(self, title)`**  
  Suggests books with titles similar to the given title.  
  **Parameters:**  
  - `title` (string): The search query.  
  **Returns:**  
  - (list): A list of similar Book objects (with a Levenshtein distance less than 6).

---

## Tests Overview

### Block (Unit) Tests

#### **TestBook**

| Test Name            | Test Type | Input Data                                    | Expected Result                                                    |
|----------------------|-----------|-----------------------------------------------|--------------------------------------------------------------------|
| `test_get_info`      | Positive  | A Book object                                 | Returns: `"1984 by George Orwell"`                                 |
| `test_change_status` | Positive  | A Book object with `available = True`         | Changes status to `False`                                          |
| `test_validate_data` | Negative  | Title: `""`, Author: `""`                      | Raises `ValueError`                                                |

#### **TestLibrary**

| Test Name                      | Test Type | Input Data                                                              | Expected Result                                                                      |
|--------------------------------|-----------|-------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| `test_add_book`                | Positive  | Title: `"The Great Gatsby"`, Author: `"F. Scott Fitzgerald"`            | Book is created and added to the library.                                            |
| `test_remove_book`             | Positive  | A Book `"To Kill a Mockingbird"` exists in the library                  | The book is removed from the library.                                                |
| `test_find_irrelevant_book`    | Negative  | Title: `"Doom"` (non-existent)                                          | Returns `None`.                                                                      |
| `test_save_to_file`            | Positive  | Filename: `"test_library.json"`                                         | Library data is saved to `"test_library.json"`.                                      |
| `test_load_from_file`          | Positive  | Library data saved in `"test_library.json"`                             | Library data is successfully loaded from the file.                                   |
| `test_levenstein_distance`     | Positive  | Strings: `"The Great Gatsby"`, `"Thee Greats atsby"`                    | Returns `3`.                                                                         |
| `test_suggest_books`           | Positive  | Books: `"Lucky man"`, `"Lucky men"`; Search: `"Lucky m"`                | Returns 2 Book objects as suggestions.                                               |
| `test_suggest_empty_title_book`| Negative  | Search query: `""`                                                      | Returns an empty list.                                                               |
| `test_find_empty_title_book`   | Negative  | Search query: `""`                                                      | Returns `None`.                                                                      |

#### **TestMember**

| Test Name                      | Test Type | Input Data                                       | Expected Result                                                      |
|--------------------------------|-----------|--------------------------------------------------|----------------------------------------------------------------------|
| `test_borrow_book`             | Positive  | A Book object and a Member object                | Book is added to the member's borrowed list.                         |
| `test_return_book`             | Positive  | A Book object and a Member object                | Book is removed from the member's borrowed list.                     |
| `test_return_not_borrowed_book`| Negative  | A Book object and a Member object (book not borrowed) | Returns a notification that the member did not borrow the book.      |
| `test_validate_data`           | Negative  | A Member object with name `""`                   | Raises `ValueError`.                                                 |

---

### Integration Tests

For these tests, a **Library** object is used with the following items:

**Books:**
- `book`: `"To Kill a Mockingbird"` by `"Harper Lee"`
- `book1`: `"1984"` by `"George Orwell"`
- `book2`: `"Brave New World"` by `"Aldous Huxley"`

**Members:**
- `member`: `"Alice"`
- `member1`: `"Kate"`
- `member2`: `"Bob"`

| Test Name                       | Test Type | Input Data                                          | Expected Result                                                                             |
|---------------------------------|-----------|-----------------------------------------------------|---------------------------------------------------------------------------------------------|
| `test_borrow_and_check_borrower`| Positive  | A Book and a Member                               | Book's status becomes `False`; added to the member's list.                                  |
| `test_return_and_check_borrower`| Positive  | A Book and a Member                               | Book's status becomes `True`; removed from the member's list.                               |
| `test_borrow_deleted_book`      | Negative  | Title: `"1984"`, Member                             | Book `"1984"` is removed; notification indicates it is unavailable.                        |
| `test_return_unborrowed_book`   | Negative  | A Book and a Member (when the book wasn't borrowed)| No changes; notification states that the member did not borrow the book.                     |
| `test_save_and_restore_with_active_loans` | Positive | A Book, another Book, a Member, Filename: `"test_library.json"` | Library is restored with all changes (loans and returns) intact.                |
| `test_suggest_add_suggest_book` | Positive  | `book1` exists; add new Book `"To Kill a Mocking guy"`; Search: `"To Kill a Mocking"` | Suggestions increase from 1 to 2 after adding the new book.                        |

---

### Attestation Tests

For these tests, the **Library** is set up with:

**Books:**
- `book`: `"To Kill a Mockingbird"` by `"Harper Lee"`
- `book1`: `"The War"` by `"Guy"`
- `book2`: `"Wars"` by `"Guy"`
- `book3`: `"WarStoke"` by `"Guy"`
- `book4`: `"War Stakes"` by `"Guy"`

**Members:**
- `member`: `"Alice"`
- `member1`: `"Kate"`
- `member2`: `"Bob"`

| Test Name              | Test Type | Input Data                                                                                                     | Expected Result                                                                                                       |
|------------------------|-----------|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `test_full_workflow`   | Positive  | New member name; new book's title and author                                                                   | A new member and book are added; the book is borrowed and then successfully returned.                                |
| `test_borrow_conflict` | Negative  | `member1` and `member2` attempt to borrow the same book (`book`)                                                 | Once borrowed by Kate, the book remains with Kate when Bob attempts to borrow it.                                     |
| `test_user_find_book`  | Positive  | User queries: `"War"`, `"WarSto"`, `"WarStoke"` using books `book1`, `book2`, `book3`, and `book4`                | For `"War"`: returns `book1`, `book2`, `book3`; for `"WarSto"`: returns `book2`, `book3`, `book4`; for `"WarStoke"`: returns only `book3`. |

---
