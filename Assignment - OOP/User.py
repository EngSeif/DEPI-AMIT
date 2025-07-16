class User:
    """
    This class represents a User
    
    Attributes :
        idx: unique id of user
        name: name of user
        role: role of user in the system
        borrowed_books: list of books that user borrowed
        
    Methods :
        init(): to set initial values
        str(): so we can print the book nicely
        borrow_book(): make user borrow books
        return_book(): return borrowed books
        print_user_borrowed_books(): print books borrowed by user
        get_role(): return User Role
    """
    
    # Class Attrubute for Assigning Unique id to used
    idx = 0

    def __init__(self, name, role):
        """
        Initializes a new Book object.

        Args:
            idx: unique id of user
            name: name of user
            role: role of user in the system
            borrowed_books: list of books that user borrowed
        """
        User.idx += 1
        self.__idx = User.idx
        self.name = name
        self.role = role
        self.borrowed_books = []

    def __str__(self):
        """
        Returns a formatted string with User information.

        Returns:
            str: Summary of the User.
        """
        return f"""
            === User Details ===
            ID   : {self.__idx}
            Name : {self.name}
            Role : {self.role}
        """
        
    def borrow_book(self, book, library):
        """
        Borrows A book from library
        
        Attributes:
            book - book to be borrowed
            library - library to borrow book from
            
        Description:
            check if book is borrowed first
                - if so, refuses borrowing
                - if not allowes borrowing
            
            if book not found in library propmts to user warning

        Returns: None
        """
        for b in library.book_list:
            if b == book:
                if b.is_borrowed == True:
                    print("Book is Already Borrowed")
                    return
                else:
                    self.borrowed_books.append(book)
                    b.is_borrowed = True
                    print(f"Book is Borrowed Sucessfully By : {self.name} ({self.role})")
                    return
        print(f"Book ({book.bookname}) Not Found In this Library")
        
    def return_book(self, book, library):
        """
        Returns A book to library
        
        Attributes:
            book - book to be Returned
            library - library to retunr book to
            
        Description:
            check if book is borrowed first
                - if so, allows returning
                - if not, disallows returning
            
            if book not found in library propmts to user warning

        Returns: None
        """
        for b in library.book_list:
            if b == book:
                if b.is_borrowed == False:
                    print("Book is Not Borrowed, Cannot Be Returned")
                    return
                else:
                    self.borrowed_books.remove(book)
                    b.is_borrowed = False
                    print(f"Book is Returned Sucessfully By : {self.name} ({self.role})")
                    return
        print(f"Book ({book.bookname}) Not Found In this Library")

    def print_user_borrowed_books(self):
        """
        Prints Books Borrowed By user
        if no books borrowed print empty
        Returns: None
        """
        print(f"\n=== User Borrowed Books ===\n")
        if len(self.borrow_books) == 0:
            print("\nNo Books Borrowed\n")
        else:
            for b in self.borrowed_books:
                print(b)

    def get_role(self):
        """
        Gets User Role
        
        Returns : role (str)
        """
        return self.role
