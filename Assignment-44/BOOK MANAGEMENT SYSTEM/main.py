import models.book
book=[]
for i in range(1,6):
    id=int(input("enter the id:"))
    name=input("enter the name :")
    author=input("enter the author name:")
    price=int(input("enter the price:"))
    b=models.book.Book(id,name,author,price)
    book.append(b)

print("------display all books-------")
for i in book:
    i.display()

print("--------search book-----")
search=int(input("enter the id of book:"))
for i in book:
    if i.book_id==search:
        i.display()

print("------display authorr------")
author=input("enter the author name:")
for i in book:
    if i.author==author:
        i.display()

print("--------greater than 500------")
for i in book:
     if i.price > 500:
         i.display()


print("-------most expensive book-------")
exp=book[0]
for i in book:
    if i.price > exp.price:
        exp=i
exp.display()

print("----------average bookk----")
total=0
for i in book:
    total+=i.price
print(total/len(book))
