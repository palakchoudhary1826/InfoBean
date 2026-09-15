'''
Question 5: Student Registration System – Longest Name

A school is organizing an inter-school cultural event. During the registration process, the coordinator notices that some students have very long names, which may not fit properly on the printed ID cards.

As a software developer, your task is to write a Python program that identifies the student with the longest name from the list of registered students using the reduce() function along with a lambda expression.

Input:
students = ["Riya", "Christopher", "Aman", "Neha", "Siddharth"]

Expected Output:
Student with the longest name: Christopher
'''

long=""

def Longest_name(i,std):
    global long   

    if len(std)==i:
        return
    
    if len(std[i])>len(long):
        long=std[i]
    Longest_name(i+1,std)


std = ["Riya", "Christopher", "Aman", "Neha", "Siddharth"]
Longest_name(0,std)
print(long)
    
