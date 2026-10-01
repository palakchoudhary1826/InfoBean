'''============================================================
ASSIGNMENT 3 — VEHICLE RENTAL SYSTEM
====================================
A vehicle rental company rents different types of vehicles.
Create:

Vehicle
|
+-------- Car
|
+-------- Bike
REQUIREMENTS:
1. Create Vehicle class.
Attributes:
* vehicle_number
* brand
* rent_per_day
2. Car should inherit from Vehicle.
Additional:
* number_of_seats
3. Bike should inherit from Vehicle.
Additional:
* engine_cc
4. Initialize parent data using super().
5. Create:
display_vehicle()
calculate_rent(days)
6. Override calculate_rent() in Car and Bike.
7. The child methods must call the parent calculation using super().
8. Use a property for rent_per_day.
9. Create:
@property
@rent_per_day.setter
@rent_per_day.deleter
10. rent_per_day must be greater than 0.
11. Read all information from the user.

INPUT:
Enter Vehicle Number:
Enter Brand:
Enter Rent Per Day:
Enter Vehicle Type:
1. Car
2. Bike
If Car:
Enter Number of Seats:
If Bike:
Enter Engine CC:
Enter Number of Rental Days:
SAMPLE INPUT:
Enter Vehicle Number: MP09AB1234
Enter Brand: Hyundai
Enter Rent Per Day: 1500
Enter Vehicle Type: 1
Enter Number of Seats: 5
Enter Number of Rental Days: 4
EXPECTED OUTPUT:
## Vehicle Details
Vehicle Number: MP09AB1234
Brand: Hyundai
Rent Per Day: 1500
Vehicle Type: Car
Number of Seats: 5
Rental Days: 4
Total Rent: 6000

'''
class Vehicle:
    def __init__(self,vehicle_no,brand,rent_per_day,type):
        self.vehicle_no=vehicle_no
        self.brand=brand
        self.rent_day=rent_per_day
        self.type=type
    @property   #getter
    def rent_per_day(self):
        return self.rent_day
    @rent_per_day.setter    #setter
    def rent_per_day(self,x):
        if x>0:
            self.rent_day=x
        else:
            print("Rent Must be greater than 0")
    @rent_per_day.deleter    #deleter
    def rent_per_day(self):
        del self.rent_day

    def calculate_rent(self,days):   #ye override karega car or bike ke calculate_rent function ko 
        self.total=days*self.rent_day

    def display_vehicle(self):
        if self.type=="Car":
            print(f"""Vehicle Number: {self.vehicle_no}
Brand: {self.brand}
Rent Per Day: {self.rent_per_day}
Vehicle Type: {self.type}
Number of Seats: {self.seat}
Rental Days: {self.rent_day}
Total Rent: {self.total}""")
        else:
            print(f"""Vehicle Number: {self.vehicle_no}
Brand: {self.brand}
Rent Per Day: {self.rent_per_day}
Vehicle Type: {self.type}
Engine CC: {self.engine_cc}
Rental Days: {self.rent_day}
Total Rent: {self.total}""")
class Car(Vehicle):
    def __init__(self,vehicle_number,brand,rent_day,type,seat):
        super().__init__(vehicle_number,brand,rent_day,type)
        self.seat=seat

    def calculate_rent(self,days):
        super().calculate_rent(days)

class Bike(Vehicle):
    def __init__(self,vehicle_number,brand,rent_day,type,engine_cc):
        super().__init__(vehicle_number,brand,rent_day,type)
        self.engine_cc=engine_cc

    def calculate_rent(self,days):
        super().calculate_rent(days)

number=input("Enter Vehicle Number:")
brand=input("Enter Vehicle brand")
rent=int(input("Enter Vehicle Rent:"))
print("""Enter Vehicle Type:
1. Car
2. Bike""")
v_type=int(input("Enter Vehicle Type:"))
match v_type:
    case 1:
        type="Car"
        seat=int(input("Enter Number of seats:"))
        days=int(input("Enter number of days:"))
        car = Car(number,brand,rent,type,seat)
        car.calculate_rent(days)
        car.rent_per_day
        car.display_vehicle()
    case 2:
        type="Bike"
        engine_cc=int(input("Enter Engine CC:"))
        days=int(input("Enter number of days:"))
        bike = Bike(number,brand,rent,type,engine_cc)
        bike.calculate_rent(days)
        bike.rent_per_day
        bike.display_vehicle()
    case __:
        print("Invalid Choice...")