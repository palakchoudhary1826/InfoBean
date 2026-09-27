"""
Assignment 6: Electricity Bill Calculator
An electricity board wants to calculate a customer's electricity bill based on units consumed.
Create a class ElectricityBill with the following attributes:
Consumer number
Consumer name
Units consumed
Rate per unit
Fixed charge
Create the following methods:
calculate_energy_charge() – Calculate units × rate per unit.
calculate_total_bill() – Add energy charge and fixed charge.
display_bill() – Display consumer details and bill amount.
Sample data:
Consumer Number: 501
Consumer Name: Amit
Units Consumed: 250
Rate Per Unit: 6
Fixed Charge: 100
Expected result:
Energy Charge: 1500
Total Bill: 1600
"""
class electricityBill():
    def accept(self,customer_no,customer_name,units_consumed,rate_perunit,fixed_charge):
        self.customer_no=customer_no
        self.customer_name=customer_name
        self.units_consumed=units_consumed
        self.rate_perunit=rate_perunit
        self.fixed_charge=fixed_charge
    def claculate_energy_charges(self):
        self.charges=self.units_consumed*self.rate_perunit
    def calculate_total_bill(self,energy_charges):
        self.energy_charges=energy_charges
        self.energy=self.energy_charges+self.fixed_charge
    def display(self):
        print("customer nummber=",self.customer_no)
        print("customer name=",self.customer_name)
        print("Units consumed=",self.units_consumed)
        print("Rate per unit=",self.rate_perunit)
        print("fixed charges=",self.fixed_charge)
        print("energy charges=",self.energy_charges)
        print("Total bill=",self.energy)
e=electricityBill()
e.accept(501,"amit",250,6,100)
e.claculate_energy_charges()
e.calculate_total_bill(1500)
e.display()
