"""
=========================================
8. LIBRARY BOOK ISSUE TRACKER
=========================================

A library records issued books.

books = [
    "Python",
    "Java",
    "Python",
    "C++",
    "Java",
    "Python"
]

Write a program to:

* Count how many times each book was issued.

Sample Output:
{
    'Python': 3,
    'Java': 2,
    'C++': 1
}
"""
books=list(map(str,input("Enter The books : ").split()))
print(books)
print()

d={}
for i in books:
    d[i]=d.get(i,0)+1

print(d)

