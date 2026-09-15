"""
=========================================
7. ONLINE EXAM RESULT SYSTEM
=========================================

Store student marks in a dictionary.

results = {
    "Ajay": 88,
    "Ravi": 45,
    "Neha": 76,
    "Aman": 39
}

Write a program to:

* Display names of students who passed.
* Passing Marks = 50

Sample Output:
Ajay
Neha
"""

n = int(input("Enter The No. of Students : "))

d = {}
p = {}

for i in range(n):
    name, marks = input(
        "Enter Student Name and Marks : "
    ).split()

    d[name] = d.get(name, 0) + int(marks)

print("Student Dictionary :")
print(d)

for k, v in d.items():
    if v >= 50:
        p[k] = v

print("Passed Students :")

for k, v in p.items():
    print(f"{k} : {v}")

