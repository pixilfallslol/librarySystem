class Author:
    def __init__(self,name):
        self.name = name

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_borrowed = False # is borrowed? False

    def borrowing(self):
        if not self.is_borrowed: # Checks if the book isnt borrowed
            self.is_borrowed = True # is borrowed? Yes
            return True # Success
        return False # Wasn't a success, the book is already borrowed
    def returning(self):
        if self.is_borrowed: # checks if the book is currently borrowed
            self.is_borrowed = False # is borrowed? not anymore!
            return True # Success
        return False # Wasn't a success, the book isn't borrowed so you can't return it


class Library:
    def __init__(self):
        self.books = [
            Book("Matilda",Author("Roald Dahl")),
            Book("Restart", Author("Gordon Korman")),
            Book("Tumtum & Nutmeg: Adventures Beyond Nutmouse Hall ",Author("Emily Bearn")),
            Book("Hatchet", Author("Gary Paulsen")),
            Book("Fish in a Tree", Author("Linda Mullaly Hunt"))
        ]
    # def addbook(self, title,author):
    #     self.books.append(Book(title,Author(author)))



    def display_books(self):
        for i, book in enumerate(self.books):
            if not book.is_borrowed:
                Status = "Available"
            else:
                Status = "Borrowed"
            print(f"{i+1}. {book.title} by {book.author.name} -- {Status}")
    def borrow_book(self,book_number):
        if 0<= book_number <len(self.books):
            if self.books[book_number].borrowing():
                print(f"You've borrowed {self.books[book_number].title}.")

            else:
                pass
        else:
            print("Invalid book number")


    def returnBook(self, book_number):
        if 0 <= book_number < len(self.books):
            if self.books[book_number].returning():
                print(f"Returned Book {self.books[book_number].title}")
            else:
                print(f"{self.books[book_number].title} was not borrowed")
        else:
            print("Invalid book number!")



def drawMenu():
    library = Library()
    while True:
        print("\nLibrary Menu-\n1. Display Books\n2. Borrow Books\n3. Return a Book\n4. Exit")
        choice = input("Choose a option (1-4)\n")
        if choice == "1":
            library.display_books()
        elif choice == "2":
            bookNum = int(input("Enter a number of the book you want to borrow: "))
            library.borrow_book(bookNum)
        elif choice == "3":
            bookNum = int(input("Enter a number of the book you want to borrow: "))
            library.returnBook(bookNum)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            break

drawMenu()
