Class Book
Description

The Book class represents a book in the library system. It allows you to store and process information about the book's title, author, availability, and its current borrower.
Attributes

    title (string): The title of the book.
    author (string): The author of the book.
    available (boolean): The availability status of the book. True if the book is available for borrowing, otherwise False.
    borrower (string or None): The name of the current borrower if the book is checked out. If the book is available, the value is None.

Methods

    __init__(self, title, author)
    Initializes the book object with the given title and author.
    Parameters:
        title (string): The title of the book.
        author (string): The author of the book.

    get_info(self)
    Returns the information about the book as a string.
    Returns:
        (string): The title of the book along with the author's name.

    change_status(self, status, borrower=None)
    Changes the availability status of the book and sets the borrower’s name if the book is checked out.
    Parameters:
        status (boolean): The new availability status.
        borrower (string, optional): The name of the borrower if the book becomes unavailable.
        Returns:
        (string): A message indicating that the status has been changed.

    _validate_data(self) (Protected)
    Validates the book's data.
    Exceptions:
        Raises ValueError if the title or author is not provided.

Class Member
Description

The Member class represents a library user who can borrow books. It stores information about the books borrowed by the user and provides methods for borrowing and returning them.
Attributes

    name (string): The name of the library user.
    borrowed_books (list of Book objects): A list of books that the member has borrowed.

Methods

    __init__(self, name)
    Initializes the member object with the given name.
    Parameters:
        name (string): The name of the user.

    borrow_book(self, book)
    Adds the book to the user's list of borrowed books if it is available.
    Parameters:
        book (Book object): The book that the user wishes to borrow.
        Returns:
        (string): A message indicating that the book was successfully borrowed or that it is unavailable.

    return_book(self, book)
    Returns the book by removing it from the user's list of borrowed books.
    Parameters:
        book (Book object): The book that the user wants to return.
        Returns:
        (string): A message indicating that the book was successfully returned or that the book was not borrowed by the user.

    _validate_data(self) (Protected)
    Validates the user's data.
    Exceptions:
        Raises ValueError if the user's name is not provided.

Class Library
Description

The Library class represents a library that manages books and users. It allows adding and removing books, registering members, and saving/loading the library's information to/from a JSON file.
Attributes

    books (list): A list of all the books in the library.
    members (list): A list of all the library members.

Methods

    __init__(self)
    Initializes the library object with empty lists for books and members.

    add_book(self, book)
    Adds a book to the library.
    Parameters:
        book (Book object): The book to be added to the library.
        Returns:
        (string): A message indicating that the book has been added.

    remove_book(self, title)
    Removes a book from the library by its title. The book becomes unavailable and its borrower is reset.
    Parameters:
        title (string): The title of the book to remove.
        Returns:
        (string): A message indicating that the book has been removed or that the book was not found.

    add_member(self, member)
    Adds a user to the library.
    Parameters:
        member (Member object): The member to be added.
        Returns:
        (string): A message indicating that the member has been added.

    _find_book(self, title) (Protected)
    Searches for a book in the library by its title.
    Parameters:
        title (string): The title of the book to find.
        Returns:
        (Book object, list of Book objects, or None): Returns a Book object if found; a list of similar books if not an exact match but similar titles exist; or None if not found at all.

    _find_member(self, name) (Protected)
    Searches for a member in the library by their name.
    Parameters:
        name (string): The name of the member to find.
        Returns:
        (Member object or None): Returns the Member object if found, or None otherwise.

    save_to_file(self, filepath)
    Saves the library's information (books and members) to a JSON file.
    Parameters:
        filepath (string): The path to the file where the information will be saved.
        Returns:
        (string): A message indicating that the information has been successfully saved.

    load_from_file(self, filepath)
    Loads the library's information (books and members) from a JSON file.
    Parameters:
        filepath (string): The path to the file from which to load the information.
        Returns:
        (string): A message indicating that the information has been successfully loaded.

    _levenshtein_distance(self, s1, s2)
    Computes the Levenshtein distance between two strings.
    Parameters:
        s1 (string): The first string for comparison.
        s2 (string): The second string for comparison.
        Returns:
        (number): The Levenshtein distance between s1 and s2.

    suggest_books(self, title)
    Finds books whose titles are similar to the given title.
    Parameters:
        title (string): The title used to search for similar books.
        Returns:
        (list): A list of Book objects whose titles are similar (with a Levenshtein distance of less than 6).

Tests
Block (Unit) Tests
Class: TestBook
Test Name	Test Type	Input Data	Expected Result
test_get_info	Positive	A Book object	Outputs book information in the format: "1984 by George Orwell"
test_change_status	Positive	A Book object with available = True	Changes the status to False
test_validate_data	Negative	Title: "", Author: ""	Raises ValueError

For the following tests (TestLibrary, TestIntegration, TestAttestation), a Library object is used to perform operations on books and members.
Class: TestLibrary
Test Name	Test Type	Input Data	Expected Result
test_add_book	Positive	Title: "The Great Gatsby", Author: "F. Scott Fitzgerald"	A Book object is created and added to the library.
test_remove_book	Positive	A Book object "To Kill a Mockingbird" exists in the library	The Book object is removed from the library.
test_find_irrelevant_book	Negative	Title of a non-existent book: "Doom"	Returns None.
test_save_to_file	Positive	Filename for saving: "test_library.json"	The library data is saved to "test_library.json".
test_load_from_file	Positive	Library data previously saved in "test_library.json"	The library data is successfully loaded from "test_library.json".
test_levenstein_distance	Positive	String1: "The Great Gatsby", String2: "Thee Greats atsby"	Returns 3.
test_suggest_books	Positive	Books in the library: "Lucky man", "Lucky men"; Search query: "Lucky m"	Returns 2 Book objects as suggestions.
test_suggest_empty_title_book	Negative	Search query: ""	Returns an empty list.
test_find_empty_title_book	Negative	Search query: ""	Returns None.
Class: TestMember
Test Name	Test Type	Input Data	Expected Result
test_borrow_book	Positive	A Book object and a Member object	The book is added to the member's borrowed list.
test_return_book	Positive	A Book object and a Member object	The book is removed from the member's borrowed list.
test_return_not_borrowed_book	Negative	A Book object and a Member object (when the book was not borrowed)	Returns a notification that the member did not borrow that book.
test_validate_data	Negative	A Member object with name ""	Raises ValueError.
Integration Tests
Class: TestIntegration

For these tests, the following objects are added to a Library object:

Books:

    book (Title: "To Kill a Mockingbird", Author: "Harper Lee")
    book1 (Title: "1984", Author: "George Orwell")
    book2 (Title: "Brave New World", Author: "Aldous Huxley")

Members:

    member (Name: "Alice")
    member1 (Name: "Kate")
    member2 (Name: "Bob")

Test Name	Test Type	Input Data	Expected Result
test_borrow_and_check_borrower	Positive	A Book object and a Member object	The book's status changes to False and the book is added to the member's list.
test_return_and_check_borrower	Positive	A Book object and a Member object	The book's status changes to True and the book is removed from the member's list.
test_borrow_deleted_book	Negative	Title: "1984", Member object	The book "1984" is removed from the library; a notification is returned indicating that the book is unavailable.
test_return_unborrowed_book	Negative	A Book object and a Member object (when the book was not borrowed)	No changes occur; a notification is returned stating that the member did not borrow the book.
test_save_and_restore_with_active_loans	Positive	A Book object, another Book object, a Member object, and filename "test_library.json"	The library is restored from the file with all changes (loans and returns) intact.
test_suggest_add_suggest_book	Positive	book1 is present; a new book "To Kill a Mocking guy" is added; search query: "To Kill a Mocking"	The number of suggested books increases from 1 to 2 after adding the new book.
Attestation Tests
Class: TestAttestation

For these tests, the following objects are used in the Library:

Books:

    book (Title: "To Kill a Mockingbird", Author: "Harper Lee")
    book1 (Title: "The War", Author: "Guy")
    book2 (Title: "Wars", Author: "Guy")
    book3 (Title: "WarStoke", Author: "Guy")
    book4 (Title: "War Stakes", Author: "Guy")

Members:

    member (Name: "Alice")
    member1 (Name: "Kate")
    member2 (Name: "Bob")

Test Name	Test Type	Input Data	Expected Result
test_full_workflow	Positive	New member name, and new book's title and author	A new member and a new book are added; the book is borrowed by the member and then returned successfully.
test_borrow_conflict	Negative	member1 and member2 attempt to borrow the same book (book)	The book, once borrowed by Kate, remains with Kate when Bob attempts to borrow it.
test_user_find_book	Positive	User queries: "War", "WarSto", "WarStoke" using the books book1, book2, book3, and book4	For the first query, recommendations include book1, book2, and book3; for the second, book2, book3, and book4; for the third, only book3.