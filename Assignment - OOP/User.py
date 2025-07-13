class User:
    idx = 0

    def __init__(self, name, role):
        User.idx += 1
        self.__idx = User.idx
        self.name = name
        self.role = role
        self.borrowed_books = []

    def __str__(self):
        return f"""
            === User Details ===
            ID   : {self.__idx}
            Name : {self.name}
            Role : {self.role}
        """
        
    def borrow_book(self, book, library):
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
        print(f"\n=== User Borrowed Books ===\n")
        if len(self.borrow_books) == 0:
            print("\nNo Books Borrowed\n")
        else:
            for b in self.borrowed_books:
                print(b)

    def get_role(self):
        return self.role
