class Book:
    def __init__(self, author, publish_year, bookname, isbn, is_borrowed):
        self.author = author
        self.publish_year = publish_year
        self.bookname = bookname
        self.__isbn = isbn
        self.is_borrowed = is_borrowed 
        
    def info(self):
        print("=== Book Details === \n")
        print(f"Author       : {self.author}")
        print(f"Publish Year : {self.publish_year}")
        print(f"Book Name    : {self.bookname:}")
        print(f"ISBN         : {self.__isbn:}")

    def __str__(self):
        return f"""
            Author       : {self.author}
            Publish Year : {self.publish_year}
            Book Name    : {self.bookname}
            ISBN         : {self.__isbn}
            Borrowed     : {self.is_borrowed}
        """

    def __eq__(self, b2):
        return self.bookname == b2.bookname
        
    # Setter
    def set_isbn(self, isbn):
        self.__isbn = isbn 
    
    # Getter
    def get_isbn(self):
        return self.__ispn