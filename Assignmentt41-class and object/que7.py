"""Assignment 7: Mobile Phone Data Usage

A mobile user wants to calculate their remaining internet data.

Create a class MobilePlan with the following attributes:

Customer name

Mobile numb

Total data in GB

Used data in GB

Validity in days

Create the following methods:

calculate_remaining_data() – Calculate remaining data.

calculate_usage_percentage() – Calculate the percentage of data used.

display_plan() – Display the plan details and results.

Sample data:

Total Data: 50 GB
Used Data: 18 GB
Validity: 28 days

Expected result:

Remaining Data: 32 GB
Usage Percentage: 36.0%"""

class mobileplan():
    def accept(self,customer_name,mobile_no,totaldata,useddata,validity):
        self.customer_name=customer_name
        self.mobile_no=mobile_no
        self.totaldata=totaldata
        self.useddata=useddata
        self.validity=validity

    def claculate_remaining_data(self):
        self.remain=self.totaldata-self.useddata
    def calculate_usage_percentage(self):
        self.percentage=(self.useddata/self.totaldata)*100
    def display(self):
        print("customer name=",self.customer_name)
        print("Mobile number=",self.mobile_no)
        print("Total data=",self.totaldata)
        print("Used data=",self.useddata)
        print("validity=",self.validity)
        print("Remaining data=",self.remain)
        print("usage percentage=",self.percentage,"%")

m=mobileplan()
m.accept("palak",234573,50,18,28)
m.claculate_remaining_data()
m.calculate_usage_percentage()
m.display()