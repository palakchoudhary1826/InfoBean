class Student:
    def __init__(self,roll_no,name,marks):
        self.roll_no=roll_no
        self.name=name
        self.marks=marks
    def display(self):
        print(f"{self.roll_no} {self.name}{self.marks}")
