"""
=========================================
4. STUDENT GRADE ANALYSIS
=========================================

Store student marks in a dictionary.

students = {
    "Ajay": 78,
    "Ravi": 92,
    "Neha": 85,
    "Aman": 65
}

Write a program to:

* Find the student with highest marks.
* Find the student with lowest marks.

Sample Output:
Highest Marks : Ravi 92
Lowest Marks : Aman 65
"""


n=int(input("Enter The Number Of Student : "))
d={}
for i in range(n):
    name=input("Enter The Name Of Student  : ")
    marks=int(input("Enter The Marks Of Student  : "))

    d[name]=d.get(name,0)+marks


print("Dictionary ", d)
high=0
highKey=''
low=list(d.values())[0]
lowKey=''

for k,v in d.items():
    if v>high:
        high=v
        highKey=k
    
    if v<low:
        low=v
        lowKey=k

print(f"Highest Score  {high} of  {highKey}")
print(f"lowest  Score  {low}  of  {lowKey}")

    