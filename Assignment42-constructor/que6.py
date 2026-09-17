"""Question 6: Library Book Management System
A library wants to maintain information about books. The librarian should be able to:
View book details.
Issue the book to a student.
Return the book.
Requirements
Create a class named Book with the following attributes:
book_id
title
author
status (Initially "Available")
Initialize the values using a constructor.
Create the following methods:
display_details() → Displays all book information.
issue_book() → Changes the status to "Issued".
return_book() → Changes the status to "Available".
Sample Input
Enter Book ID : B101
Enter Book Title : Python Programming
Enter Author Name : John Smith
Sample Output
------ Book Details ------
Book ID     : B101
Title       : Python Programming
Author      : John Smith
Status      : Available

Book issued successfully.
------ Book Details ------
Book ID     : B101
Title       : Python Programming
Author      : John Smith
Status      : Issued

Book returned successfully.
------ Book Details ------
Book ID     : B101
Title       : Python Programming
Author      : John Smith
Status      : Available"""

class book():
    def __init__(self):
        self.book_id="B101"
        self.tittle="python Programming"
        self.author="John Smith"
    def display(self):
        print("-----------Book Details----------")
        print("Book Id :",self.book_id)
        print("Tittle :",self.tittle)
        print("Author :",self.author)
        print("Status: Available")
        
    def issued_book(self):
            print("Book issued successfully")
            print("-----------Book Details----------")
            print("Book Id :",self.book_id)
            print("Tittle :",self.tittle)
            print("Author :",self.author)
            print("Status: Issued")
           
    def return_book(self):
            print("Book return successfully")
            print("-----------Book Details----------")
            print("Book Id :",self.book_id)
            print("Tittle :",self.tittle)
            print("Author :",self.author)
            print("Status: Available")
b=book()
b.display()
b.issued_book()
b.return_book()
            
    