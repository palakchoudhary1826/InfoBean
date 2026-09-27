"""Assignment 8: Car Mileage Calculator
 A car owner wants to calculate the mileage and fuel cost of a journey.
Create a class Car with the following attributes:
Car brand
Car model
Distance travelled in km
Fuel consumed in litres
Petrol price per litre
Create the following methods:
calculate_mileage() – Calculate kilometres per litre.
calculate_fuel_cost() – Calculate total fuel cost.
display_trip_details() – Display car and journey details.
Formulas:
Mileage = Distance / Fuel Consumed
Fuel Cost = Fuel Consumed × Petrol Price
Sample data:
Car Brand: Maruti
Car Model: Swift
Distance: 320 km
Fuel Consumed: 20 litres
Petrol Price: 105
"""

class car():
    def accept(self,car_brand,car_model,distance,fuel,petrol):
        self.car_brand=car_brand
        self.car_model=car_model
        self.distance=distance
        self.fuel=fuel
        self.petrol=petrol
    def calculate_mileage(self):
        self.mileage=self.distance/self.fuel
    def calculate_fuel_cost(self):
        self.fuel_cost=self.fuel*self.petrol
    def display(self):
        print("car brand=",self.car_brand)
        print("car model=",self.car_model)
        print("distance=",self.distance)
        print("fuel consumed",self.fuel)
        print("petrol price=",self.petrol)
        print("Mileage=",self.mileage)
        print("fuel cost=",self.fuel_cost)
c=car()
c.accept("maruti","swift",320,20,105)
c.calculate_mileage()
c.calculate_fuel_cost()
c.display()