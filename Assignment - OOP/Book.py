class Book:
    """
    This class represents a real book
    
    Attributes :
        title: name of the book
        author: who wrote it
        year: year it was published
        isbn: private unique book ID
        is_borrowed: to track if someone borrowed the book (True/False)
        
    Methods :
        init(): to set initial values
        str(): so we can print the book nicely
        set_isbn() and get_isbn() to safely access the private ISBN
    """

    def __init__(self, author, publish_year, bookname, isbn, is_borrowed):
        """
        Initializes a new Book object.

        Args:
            title: name of the book
            author: who wrote it
            year: year it was published
            isbn: private unique book ID
            is_borrowed: to track if someone borrowed the book (True/False)
        """
        self.author = author
        self.publish_year = publish_year
        self.bookname = bookname
        self.__isbn = isbn
        self.is_borrowed = is_borrowed 
        
    def info(self):
        """
        Prints a formatted string with book information.

        Returns: None
        """
        print("=== Book Details === \n")
        print(f"Author       : {self.author}")
        print(f"Publish Year : {self.publish_year}")
        print(f"Book Name    : {self.bookname:}")
        print(f"ISBN         : {self.__isbn:}")

    def __str__(self):
        """
        Returns a formatted string with book information.

        Returns:
            str: Summary of the book.
        """
        return f"""
            Author       : {self.author}
            Publish Year : {self.publish_year}
            Book Name    : {self.bookname}
            ISBN         : {self.__isbn}
            Borrowed     : {self.is_borrowed}
        """

    def __eq__(self, b2):
        """
        Overrides The == Operator And Compare Books
        By Book Name
        
        Return  : True if Same Bookname
                  False if Not Same Bookname
        """
        return self.bookname == b2.bookname
        
    # Setter
    def set_isbn(self, isbn):
        """
        Set isbn by user
        
        Attributes:
            - isbn : id of book
        
        Return None
        """
        self.__isbn = isbn 
    
    # Getter
    def get_isbn(self):
        """
        Get isbn of Book
        
        Return : isbn of book
        """
        return self.__isbn