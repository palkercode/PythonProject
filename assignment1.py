books = [
    {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "year": 1988,
        "copies_available": 5
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year": 1960,
        "copies_available": 3
    },
]

def is_book_valid(title, author, year):
    if title == "" or author == "" or year.isalpha() or int(year) < 0:
        return False
    return True

def add_book():
    title = input("Enter a title: ")
    author = input("Enter an author: ")
    year = input("Enter a year: ")
    
    if not is_book_valid(title, author, year):
        print("The book format is invalid!")    
        return add_book()
    
    for book in books:
        if title == book["title"]:
            book["copies_available"] += 1
            return
        
    books.append({
        "title": title,
        "author": author,
        "year": year,
        "copies_available": 1
    })

def search_book():
    title = input("Enter a title of a book you want to find: ")
    
    for book in books:
        if book["title"] == title:
            print("Book found! Book title is {0}, its author is {1}, year {2}, and there are {3} copies available".format(book["title"], book["author"], book["year"], book["copies_available"]))
            return
    print("The book was not found")
    
def borrow_book():
    title = input("Enter a title of a book you want to borrow: ")
    
    for book in books:
        if book["title"] == title:
            book["copies_available"] -= 1
            return
    
    print("The book was not found")

def return_book():
    title = input("Enter a title of a book you want to return: ")
    
    for book in books:
        if book["title"] == title:
            book["copies_available"] += 1
            return
    
    print("The library does not have this book")

def view_all_books():
    print("Title", "Author", "Year", "Copies", sep="     ")
    print("----------------------------------")
    
    for book in books:
        print(book["title"], book["author"], book["year"], book["copies_available"], "\n", sep="     ")

def ask_for_action():
    action = input("Enter an action (add, search, borrow, return, viewall, exit): ")
    
    if action == "add":
        add_book()
    elif action == "search":
        search_book()
    elif action == "borrow":
        borrow_book()
    elif action == "return":
        return_book()
    elif action == "viewall":
        view_all_books()
    elif action == "exit":
        exit()
    else:
        print("Invalid operation!")

while (True):
    ask_for_action()