"""Question 3: Online Shopping System
Scenario
An e-commerce company wants to calculate the final amount payable by customers after applying discounts.
Requirements
Create a class named Product with:
product_id
product_name
quantity
price_per_item
Initialize the values using a constructor.
Calculations
Total Amount = Quantity × Price Per Item
If Total Amount > ₹5000, Discount = 10%
Otherwise, Discount = 5%
Final Amount = Total Amount − Discount
Sample Input
Enter Product ID : P101
Enter Product Name : Laptop
Enter Quantity : 2
Enter Price Per Item : 35000
Sample Output
------ Shopping Bill ------
Product ID        : P101
Product Name      : Laptop
Quantity          : 2
Price Per Item    : 35000.0
Total Amount      : ₹70000.0
Discount          : ₹7000.0
Final Amount      : ₹63000.0"""

class product():
    def __init__(self):
        self.pro_id="p101"
        self.pro_name="laptop"
        self.quantity=2
        self.price_per_item=35000
        self.total_amount=self.quantity*self.price_per_item
        if self.total_amount > 5000:
            self.dis=self.total_amount*10/100
        else:
            self.dis=self.total_amount*5/100
        self.final_amount=self.total_amount-self.dis
    def display(self):
        print("Product id:",self.pro_id)
        print("Product name",self.pro_name)
        print("Quantity:",self.quantity)
        print("price per item:",self.price_per_item)
        print("Total Amount:",self.total_amount)
        print("Discount:",self.dis)
        print("Final Amount:",self.final_amount)

p=product()
p.display()