from Book import Book

class Library:

    def __init__(self):
        self.book_list = []

    def add_book(self, book, User):
        if User.get_role().lower() == "librarian":
            if (isinstance(book, Book)):
                self.book_list.append(book)
                print(f"✅ Book {book.bookname} added to library.")
            else:
                print("Enter A Valid Book Object")
        else:
            print("⚠️ Warning : Only A Librarian Can Add Books")

    def remove_book(self, title, User):
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
        print("\n=== Books in Lib ===\n")
        if len(self.book_list) == 0:
            print("\nNo Books In Library\n")
        else:
            for b in self.book_list:
                print(b)

    def find_book_by_title(self, title):
        for b in self.book_list:
            if b.bookname == title:
                return b
        print(f"⚠️ Book {title} not found.")
        return None
