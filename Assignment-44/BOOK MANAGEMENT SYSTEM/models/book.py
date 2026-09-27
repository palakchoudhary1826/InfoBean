class Book:
    def __init__(self,book_id,book_name,author,price):
        self.book_id=book_id
        self.book_name=book_name
        self.author=author
        self.price=price
    def display(self):
        print(f"{self.book_id}{self.book_name}{self.author}{self.price}")
    