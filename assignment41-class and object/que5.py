"""
Assignment 5: Shopping Bill Calculator
 A retail shop wants to calculate the total bill for a customer.
Create a class ShoppingBill with the following attributes:
Product name
Product price
Quantity
Discount percentage
GST percentage
Create the following methods:
calculate_subtotal() – Calculate price × quantity.
calculate_discount() – Calculate the discount amount.
calculate_gst() – Calculate GST on the discounted amount.
calculate_final_bill() – Calculate the final payable amount.
display_bill() – Display the complete bill details.
Formula:
Subtotal = Price × Quantity
Discounted Amount = Subtotal - Discount
GST = Discounted Amount × GST Percentage / 100
Final Bill = Discounted Amount + GST
"""
class shopingBill():
    def accept(self,product_name,product_price,quantity,discount_per,gst_per):
        self.product_name=product_name
        self.product_price=product_price
        self.quantity=quantity
        self.discount_per=discount_per
        self.gst_per=gst_per
    def calculate_subtotal(self):
        self.subtotal=self.product_price*self.quantity
    def calculate_discount(self):
       self.discount_amount = self.subtotal * self.discount_per / 100
       self.discounted_amount = self.subtotal - self.discount_amount

    def calculate_gst(self):
        self.gst=self.discount_amount*self.gst_per/100
    def calculate_final_bill(self):
        self.finalbill=self.discount_amount+self.gst
    def display(self):
        print("Product Name =", self.product_name)
        print("Product Price =", self.product_price)
        print("Quantity =", self.quantity)
        print("Subtotal =", self.subtotal)
        print("Discount Amount =", self.discount_amount)
        print("GST =", self.gst)
        print("Final Bill =", self.finalbill)


s=shopingBill()
s.accept("vivo",50000,2,10,18)
s.calculate_subtotal()
s.calculate_discount()
s.calculate_gst()
s.calculate_final_bill()
s.display()
