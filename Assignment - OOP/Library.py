from Book import Book

class Library:
    """
    Represents a Library For Books Operations

    Attributes:
        book_list (list) : books that are in library

    Methods:
        __init__():
            Initializes a book_list for object instance
        add_book():
            allow only librarian to add book to the library
        remove_book():
            allow only librarian to remove book from the library
        list_books():
            print books in the library
        find_book_by_title():
            find book that matches the title passed
    """

    def __init__(self):
        """
        Initialize a new Library instance with empty book list.
        """
        self.book_list = []

    def add_book(self, book, User):
        """
        Add Book to library.
        
        Attributes:
            - book : book to be added
            - User : user that will add book

        if user is librarian:
            allow him to add books
        
        prompts to user status of addition
    
        Returns: None
        """
        if User.get_role().lower() == "librarian":
            if (isinstance(book, Book)):
                self.book_list.append(book)
                print(f"✅ Book {book.bookname} added to library.")
            else:
                print("Enter A Valid Book Object")
        else:
            print("⚠️ Warning : Only A Librarian Can Add Books")

    def remove_book(self, title, User):
        """
        Remove Book from library.
        
        Attributes:
            - title : title of book to be removed
            - User  : user that will remove books

        if user is librarian:
            allow him to remove books
            if book title is not found:
                prompts to user that book is not found
        
        prompts to user status of addition
    
        Returns: None
        """
        if User.get_role().lower() == "librarian":
            for b in self.book_list:
                if b.bookname == title:
                    if b.is_borrowed:
                        print("⚠️ Book is Borrowed Cannot Be Removed")
                        return
                    else:
                        print(f"✅ Book {b.bookname} is Removed Sucessfully")
                        self.book_list.remove(b)
                        return
            print("⚠️ Warning : Book is Not FOund")
        else:
            print("⚠️ Warning : Only A Librarian Can Remove Books")

    def list_books(self):
        """
        List Books In library.

        if no books are in list, print Empty
    
        Returns: None
        """
        print("\n=== Books in Lib ===\n")
        if len(self.book_list) == 0:
            print("\nNo Books In Library\n")
        else:
            for b in self.book_list:
                print(b)

    def find_book_by_title(self, title):
        """
        find Book In library by its title.
        
        Attributes:
            - title : title of book to search for

        if book title is NOT in list, print Not FOund
    
        Returns: Book : if Book is found
                 None : if Book is NOT FOUND
        """
        for b in self.book_list:
            if b.bookname == title:
                return b
        print(f"⚠️ Book {title} not found.")
        return None
