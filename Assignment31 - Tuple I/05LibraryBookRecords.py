"""
QUESTION 5: LIBRARY BOOK RECORDS

A library maintains book information using NamedTuple.

Fields:
book_id, title, author, price

Requirements:

1. Read N book records from the user and store them in a list of NamedTuples.

2. Display all book details.

3. Find and display the most expensive book.

4. Search books by author name.

5. Calculate and display the average price of all books.

Test Case:

Input:
Enter number of books: 4

B101 Python Basics John 450
B102 Java Programming James 550
B103 Data Science John 700
B104 SQL Guide Smith 300

Enter Author Name: John

Expected Output:
Most Expensive Book:
B103 Data Science John 700

Average Book Price:
500.0

Books Written By John:
B101 Python Basics John 450
B103 Data Science John 700
"""

from collections import namedtuple


book=namedtuple("book",["book_id","title","author","price"])


n=int(input("Enter The Number of Books : "))
list=[]


for i in range(n):
    print(f"Enter Book {i+1} Details")
    id=input("Enter Book ID       : ")
    title=input("Enter Title         : ")
    author=input("Enter Author        : ")
    price=input("Enter Price         : ")
    list.append(book(id,title,author,int(price)))
    print(f"{i+1}th Book Details Stored ...")
    print()


print(list)


print("All Book Details : ")


count=1


for i in list:
    print(f"{count}th Book Details")
    print(f"Book ID    : {i.book_id}")
    print(f"Title      : {i.title}")
    print(f"Author     : {i.author}")
    print(f"Price      : {i.price}")
    count+=1
    print()


highest=list[0]
sum=0

for i in list:
    if i.price>highest.price:
        highest=i

    sum+=i.price


print("Most Expensive Book : ")
print(f"Book ID    : {highest.book_id}")
print(f"Title      : {highest.title}")
print(f"Author     : {highest.author}")
print(f"Price      : {highest.price}")


print()
print(f"Average Book Price : {sum/n}")


author=input("Enter Author Name : ")

print(f"Books Written By {author} : ")

for i in list:
    if i.author==author:
        print(f"Book ID    : {i.book_id}")
        print(f"Title      : {i.title}")
        print(f"Author     : {i.author}")
        print(f"Price      : {i.price}")
        print()