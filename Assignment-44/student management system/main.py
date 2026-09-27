import Models.student
students=[]
for i in range(5):
    roll=int(input("Enter roll number: "))
    name = input("Enter Name: ")
    marks=int(input("Enter marks: "))
    s = Models.student.Student(roll,name,marks)
    students.append(s)
for i in students:
    i.display()

print("Students having marks greater than 60:")
for i in students:
    if i.marks>=60:
        i.display()

print("Highest Marks: ")
high=students[0]
for i in students:
    if i.marks>high.marks:
        high=i
high.display()

print("Average Marks: ")
total=0
for i in students:
    total += i.marks
print(total/len(students))