class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Author(Person):
    def __init__(self, name, age, books_written):
        super().__init__(name, age)
        self.books_written = books_written

    def display_books(self):
        for book in self.books_written:
            print(book)

    def greet(self):
        print(f"Hello! My name is {self.name} and I'm an author.")

class GuestAuthor(Author):
    def __init__(self, name, age, books_written, event_topic):
        super().__init__(name, age, books_written)
        self.event_topic = event_topic

    def greet(self):
        print(f"Hello! My name is {self.name}, I'm an author and guest on event about {self.event_topic}.")

class Librarian(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def manage_library(self, library):
        return library

class LibraryMember:
    def __init__(self, member_id, borrowed_books):
        self.member_id = member_id
        self.borrowed_books = borrowed_books

    def borrow_book(self, book_title):
        self.borrowed_books.append(book_title)

class RegularMember(Person, LibraryMember):
    def __init__(self, name, age, member_id, borrowed_books):
        Person.__init__(self, name, age)
        LibraryMember.__init__(self, member_id, borrowed_books)