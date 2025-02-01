from library import Book, Shelf, Library
from people import Author, Librarian

albert_einstein = Author("Albert Einstein", 123313, 2467)
funny_author = Author("Funny author", 123313, 2467)

scientific_book_1 = Book("Cool scientific book", albert_einstein, 52)
scientific_book_2 = Book("Second cool scientific book", albert_einstein, 52)
scientific_shelf = Shelf([scientific_book_1, scientific_book_2])

funny_book_1 = Book("Funy buk", funny_author, 456757)
funny_book_2 = Book("Funy buk 2: The great sequel", funny_author, 456757)
funny_book_3 = Book("Funy buk 3: The return", funny_author, 456757)
funny_book_4 = Book("Funy buk 4: The grand final", funny_author, 456757)
funny_shelf = Shelf([funny_book_1, funny_book_2, funny_book_3, funny_book_4])

the_library = Library([])

librarian = Librarian("Name", 232, 356)
librarian.manage_library(the_library).shelves = [
    scientific_shelf,
    funny_shelf
]