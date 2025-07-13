from User import User
from Book import Book
from Library import Library
from Student import Student

# Create library

library = Library()

# Create users 

librarian = User("Alice", "Librarian") 
student = Student("Bob", 10) 

# Create books

book1 = Book("Robert C. Martin", 2008, "Clean Code", "123", False)
book1.set_isbn("123-456")

# Librarian adds the book ✅ 
library.add_book(book1, librarian) 
library.list_books()

# Student tries to add a book ❌ 
book2 = Book("John Doe", 2022,  "Intro to Python", "456", False) 
library.add_book(book2, student) 
library.list_books()

# Student borrows the book ✅
student.borrow_book(book1, library)
library.list_books()
student.print_user_borrowed_books() 

# Librarian tries to remove borrowed book ❌
library.remove_book("Clean Code", librarian)
library.list_books()
student.print_user_borrowed_books() 

# Student returns book ✅ 
student.return_book(book1, library) 
library.list_books()
student.print_user_borrowed_books() 

# Librarian removes book ✅
library.remove_book("Clean Code", librarian)
library.list_books()