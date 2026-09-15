'''
4. Scholarship Eligibility System (Using filter(), map(), and sorted() with Lambda Expressions)

A university is offering scholarships to students based on their academic performance.

The scholarship committee has decided on the following rules:
1. Only students who score 75 marks or above are eligible for the scholarship.
2. Eligible students will receive 5 bonus marks.
3. The updated marks should be displayed in descending order.

Task:
Write a Python program that:
1. Filters students who have scored 75 or above.
2. Adds 5 bonus marks to each eligible student.
3. Sorts the updated marks in descending order.
4. Displays the final list of scholarship marks.

Note:
Use filter() to select eligible students, map() to add the bonus marks, and sorted() to display the final marks in descending order. All three operations must use lambda expressions.

Input Format:
The first line contains an integer N, representing the number of students.
The second line contains N space-separated marks.

Output Format:
Display the updated scholarship marks in descending order.

Sample Input:
Enter the number of students:
8

Enter the marks:
65 80 92 74 88 76 55 95

Sample Output:
Scholarship Marks:
100 97 93 85 81
'''

def scholarship (i):
    return i+5


l=list(map(int,input("Enter Student Mark : ").split()))

MarkFilter=list(filter(lambda x : x>=75,l))
print(MarkFilter)
result=list(map(scholarship,MarkFilter))
result.sort(key=lambda x : x , reverse=True)
print(result)