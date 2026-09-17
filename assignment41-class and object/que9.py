"""Assignment 9: Product Inventory Management
A shopkeeper wants to manage the stock of a product.
Create a class Product with the following attributes:
Product ID
Product name
Price
Available quantity
Create the following methods:
add_stock() – Increase the available quantity.
sell_product() – Decrease the available quantity.
calculate_stock_value() – Calculate price × available quantity.
display_product() – Display product and stock details.
Sample operations:
Product Name: Laptop
Price: 45000
Initial Quantity: 10
Add Stock: 5
Sell Product: 3
Expected result:
Available Quantity: 12
Total Stock Value: 540000"""

class product():
    def accept(self,product_id,product_name,price,available_quality):
        self.product_id=product_id
        self.product_name=product_name
        self.price=price
        self.available_quality=available_quality
    def add_stock(self,in_stock):
        self.in_stock=in_stock
        self.stock_in=self.available_quality+self.in_stock
    def dec_stock(self,sell_pro):
        self.sell_pro=sell_pro
        self.stock_dic=self.available_quality+self.sell_pro-self.in_stock
    def calculate_stock_value(self):
        self.cal=self.price*self.available_quality
    def display(self):
        print("product name=",self.product_name)
        print("Price=",self.price)
        print("initial quality=",self.stock_dic)
        print("add stock=",self.in_stock)
        print("sell product=",self.sell_pro)
        print("available quantity=",self.available_quality)
        print("total stock value=",self.cal)
p=product()
p.accept(101,"laptop",45000,12)
p.add_stock(5)
p.dec_stock(3)
p.calculate_stock_value()
p.display()