# 🧠 Title: Build a Library Management System Using Classes in Python

## 🎯 Goal of the Task:

You will build a real-world system using the concepts of Object-Oriented Programming (OOP) in Python. The system is a Library where:

- Librarians manage books (add/remove)

- Students can borrow and return books

- Each book has basic information and status (borrowed or available)

This task will help you understand and apply:

- Classes and objects

- Inheritance

- Encapsulation (private attributes)

- Permissions (who can do what)

- How multiple classes work together

## 📦 The System Will Have Four Main Classes

### 🟦 Book class

This class represents a real book.

✅ Attributes (Variables inside the class):

- title: name of the book

- author: who wrote it

- year: year it was published

- **isbn: private unique book ID (use ** to make it private)

- is_borrowed: to track if someone borrowed the book (True/False)

✅ Methods (Functions inside the class):

- **init**(): to set initial values

- **str**(): so we can print the book nicely

- set_isbn() and get_isbn() to safely access the private ISBN

- Optional: **repr**() for debugging

### 🟩 User class

This is the general class for any person who uses the system.

✅ Attributes:

- name

- role (like "Librarian" or "Student")

- id (unique number)

- borrowed_books: list of books the user borrowed

✅ Methods:

- borrow_book(book, library) → borrow a book if available

- return_book(book, library) → return a borrowed book

- get_role() → tells you the role

- **str**() → nice print of the user

### 🟨 Student class (inherits from User)

This is a special type of user.

✅ Extra Attribute:

- grade_level (like 10th grade)

✅ Method Overrides:

- get_role() → should return “Student User”

### 🟫 Library class

This is the brain of the system. It manages all the books.

✅ Attribute:

- books: list of all books added to the library

✅ Methods:

- add_book(book, user)
  → only librarians can add
  → if student tries: show error message

- remove_book(title, user)
  → only librarians can remove, and only if the book is not borrowed

- list_books()
  → print all books in the system

- find_book_by_title(title)
  → return the book if found, else print “not found”

### 🔐 Rules for Permissions (Access Control):

Only users with role "Librarian" can:

- Add books

- Remove books (if not borrowed)

- Students are not allowed to add or remove books

- Students can borrow and return books

🧪 Sample Workflow to Test:

```
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
```
