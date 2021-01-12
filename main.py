class Library:
    def __init__(self,listofbooks):
        self.books = listofbooks

    def displayAvalaibleBooks(self):
        print("Books present in the library are: ")
        for book in self.books:
            print(book)

    def borrowBook(self,bookname):
        if bookname in self.books:
            print("Yes the "+bookname + " has been issued by you. Please take care of it and return it within 30 days.")
            self.books.remove(bookname)
            return True
        else:
            print("Sorry the book has already been issued. Please wait until it is returned. Thank You.")
            return False 

    def returnbook(self,bookname):
        self.books.append(bookname)
        print("Thank you for returning the book. We hope you had a great time reading it.")

class Student:
    def requestbook(self):
        self.book = input("Please mention the bookname you want to borrow: ")
        return self.book

    def returnbook(self):
        self.book = input("Please mention the bookname you want to return: ")    
        return self.book


if __name__ == "__main__" :
    print("Please Enter a list of books: ")
    books_ = list(map(str,input().split()))
    centralLibrary = Library(books_)
    student = Student()
    while True:
        welcmsg = '''||| WELCOME TO THE CENTRAL LIBRARY |||
        Please choose an option: 
        1. To see the available books
        2. Request a book 
        3. Return a book
        4. Exit the library  '''

        print(welcmsg)      
        c = int(input("Enter your choice : "))
        if c == 1:
            centralLibrary.displayAvalaibleBooks()
        elif c == 2:
            centralLibrary.borrowBook(student.requestbook())
        elif c == 3:
            centralLibrary.returnbook(student.returnbook())
        elif c == 4:
            print("Thank you for choosing Central Library. Have a great day ahead! ") 
            exit(0)  
        else:
            print("OOPS INVALID CHOICE! ")                   
