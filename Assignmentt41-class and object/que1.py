"""Assignment 1: Student Result Calculator

 A school wants to calculate the total marks and percentage of a student.

Create a class Student with the following attributes:

Student name

Roll number

Marks in English

Marks in Mathematics

Marks in Science

Create the following methods:

calculate_total() – Calculate the total marks.

calculate_percentage() – Calculate the percentage.

display_result() – Display student details, total, and percentage.

Expected output:

Student Name: Ajay
Roll Number: 101
Total Marks: 240
Percentage: 80.0%"""
class student:
      def accept(self,name,roll_no):
            self.name=name
            self.roll_no=roll_no
      def calulate_total(self,english,mathematics,science):
            self.english=english
            self.mathematics=mathematics
            self.science=science
            self.total=self.english+self.mathematics+self.science
      def calculate_percentage(self):
            self.percentage= self.total/3
    
      def display_result(self):
            print("student Name:",self.name)
            print("Roll No.:",self.roll_no)
            print("total marks:",self.total)
            print("percentage:",self.percentage,"%")

s1=student()
s1.accept("palak",101)
s1.calulate_total(60,90,90)
s1.calculate_percentage()
s1.display_result()



            
            