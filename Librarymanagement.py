#!/usr/bin/python3

class Library:
    def __init__(self,listOfBook):
        self.availableBook=listOfBook

    def displayAllBooks(self):
        print("Available Book=")
        for book in self.availableBook:
             print(book)
    def lendBook(self,requestedbook):
        if requestedbook in self.availableBook:
            print("you have borrow the book")
            self.availableBook.remove(requestedbook)
        else:
            print("sorry,book is not available in list")

    def addBook(self,returnBook):
        self.availableBook.append(returnBook)
        print("you have return the book ,Thankyou")

class Customer:
    def requestBook(self):
        print("Enter the name of book you would like to borrow")
        self.book=input()
        return self.book
    def returnBook(self):
        print("Enter the name of book you want to return")
        self.book=input()
        return self.book
library=Library(["Machine Learning","Java","python"])
customer=Customer()

while True:

    print("Enter 1 to display the available books")
    print("Enter 2 to display the request for a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit")
    userchoice =int(input())
    if userchoice is 1:
        library.displayAllBooks()
    elif userchoice is 2:
        requestedbook=customer.requestBook()
        library.lendBook(requestedbook)
    elif userchoice is 3:
        returnedBook=customer.returnBook()
        library.addBook(returnedBook)
    elif userchoice is 4:
        quit()
