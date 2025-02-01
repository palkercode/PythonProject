class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def get_price(self):
        return self.price

class Shelf:
    def __init__(self, books):
        self.books = books

    def add_book(self, book):
        self.books.append(book)

    def get_total_books(self):
        return len(self.books)

class Library:
    def __init__(self, shelves):
        self.shelves = shelves

    def total_books(self):
        total = 0

        for shelf in self.shelves:
            total += shelf.get_total_books()

        return total

    def show_all_books(self):
        for shelf in self.shelves:
            for book in shelf.books:
                print(book.title)
