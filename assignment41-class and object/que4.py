"""Assignment 4: Rectangle Calculator

 A civil engineer wants to calculate the area and perimeter of a rectangular plot.

Create a class Rectangle with the following attributes:

Length

Breadth

Create the following methods:

calculate_area() – Calculate the area.

calculate_perimeter() – Calculate the perimeter.

display_result() – Display length, breadth, area, and perimeter.

Formulas:

Area = Length × Breadth
Perimeter = 2 × (Length + Breadth)

Sample data:

Length: 15
Breadth: 8
"""

class rectangle:
    def calculate_area(self,length,breadth):
        self.lenght=length
        self.breadth=breadth
        self.area=self.lenght*self.breadth
    def calculate_perimeter(self):
        self.perimeter=2*(self.lenght+self.breadth)
    def display(self):
        print("Area =",self.area)
        print("perimeter=",self.perimeter)
r=rectangle()
r.calculate_area(15,8)
r.calculate_perimeter()
r.display()