"""
# Problem Statement:

## Implement a library management system with the following classes:

---

1.  Library class:

    -   Attributes:

        1. name (string)
        2. books (list of Book objects)

    -   Methods:
        1. add_book(book): Add a new book to the library.
        2. get_total_books(): Return the total number of books in the library.
        3. get_available_books(): Return the number of available books.
        4. get_borrowed_books(): Return the number of borrowed books.
        5. get_books_by_author(author): Return a list of books written by a specific author.
        6. get_books_by_genre(genre): Return a list of books in a specific genre.
        7. borrow_book(book_id, borrower): Borrow a book from the library.
        8. return_book(book_id): Return a borrowed book to the library.
        9. get_book_details(book_id): Return the details of a specific book.

2.  Book class:

    -   Attributes

        1. book_id (integer)
        2. title (string)
        3. author (string)
        4. genre (string)
        5. borrowed (boolean)

    -   Methods:
        -   None

---

#### Your task is to implement these classes and write a program to simulate the library management system. The program should allow the user to perform the following operations:

-   [] Add books to the library.
-   [] Retrieve and display the total number of books.
-   [] Retrieve and display the number of available books.
-   [] Retrieve and display the number of borrowed books.
-   [] Retrieve and display a list of books written by a specific author.
-   [] Retrieve and display a list of books in a specific genre.
-   [] Borrow a book from the library.
-   [] Return a borrowed book to the library.
-   [] Retrieve and display the details of a specific book.

**Note:** You are free to design the program structure and logic as per your understanding and preferences. The problem statement provides a basic outline of the required classes and their methods. You may add additional methods or attributes to enhance the functionality of the library management system.

"""

class Library:

    def __init__(self,name):
        self.name = name
        self.books = {}

    def add_book(self,book):
        self.books[book.book_id] = book

    def get_total_books(self):
        return len(self.books)
    
    def get_book(self,book_id):
        return self.books.get(book_id)


    def get_available_books(self):
        return len([book for book in self.books.values() if not book.borrowed])



    def get_borrowed_books(self):
        return len([book for book in self.books.values() if book.borrowed])

    def get_books_by_author(self,author):
        return [book for book in self.books.values() if book.author == author]
        # if author_book:
        #     return author_book
        # # raise Exception ("author not found ")

    def get_books_by_genre(self,genre):
        return [book for book in self.books.values() if book.genre == genre]
        # if gener_book:
        #     return gener_book
        # genre_book= [book for book in self.books if book.genre == genre]
        # for book in genre_book:
        #      print(f"Book ID: {book.book_id}, Title: {book.title},Genere: {book.genre}")
        # # raise Exception("Genere not found")

    def borrow_book(self,book_id):
        book = self.get_book(book_id)
        if book and not book.borrowed:
            book.borrowed = True
            book.borrower = borrower
            return True
        return False
    
    def return_book(self,book_id):
        book = self.get_book(book_id)
        if book and book.borrowed:
            book.borrowed = False
            book.borrower = None
            return True
        return False

    def get_book_details(self,book_id):
        # for book in self.books:
        #     if book.book_id == book_id:
        #         return f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Borrowed: {book.borrowed}"
        # return "Book not found"
        book = self.get_book(book_id)
        if book:
            return book.__dict__
        return None


class Book:
    def __init__(self,book_id,title,author,genre,borrowed,browwer=None):
        self.book_id = book_id
        self.title=title
        self.author = author
        self.genre = genre
        self.borrowed = borrowed
        # self.borrower = None





if __name__ == "__main__":
    obj_1=Book(1,"train Love","milan","romance",True)
    obj_2=Book(2,"The Last Day","ravi","fiction",False)

    obj=Library("public library")
    obj.add_book(obj_1)
    obj.add_book(obj_2)
    # print(obj.get_total_books())
    # print(obj.get_available_books())
    # print(obj.get_borrowed_books())
    print(obj.get_books_by_author("ravi"))
    # print(obj.get_books_by_genre("romance"))
    # print(obj.borrow_book(1))
    # print(obj.return_book(2))
    print(obj.get_book_details(2))
     