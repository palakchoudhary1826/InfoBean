"""Question 2: Electricity Bill Calculator
Scenario
An elecricity company wants to generate monthly bills for its customers.
Requirements
Create a class named Customer with:
customer_id
customer_name
units_consumed
Initialize the values using a constructor.
Calculations
Cost per Unit = ₹8
Fixed Charge = ₹150
Total Bill = (Units × 8) + 150
Sample Input
Enter Customer ID : C101
Enter Customer Name : Amit Verma
Enter Units Consumed : 350
Sample Output
------ Electricity Bill ------
Customer ID       : C101
Customer Name     : Amit Verma
Units Consumed    : 350
Total Bill Amount : ₹2950.0"""

class customer():
    def __init__(self):
        self.customer_id=101
        self.customer_name="Amit verma"
        self.unit_cunsumed=350
        self.cost_per_unit=8
        self.fixed_charges=150
        self.total=self.unit_cunsumed*self.cost_per_unit+self.fixed_charges
    def display(self):
        print("Customer ID  :",self.customer_id)
        print("customer name:",self.customer_name)
        print("Units consumed:",self.unit_cunsumed)
        print("total bill:",self.total)
c=customer()
c.display()
