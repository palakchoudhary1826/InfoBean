"""
Question 2: Smart City Traffic Peak Load Analyzer

Problem:
    Find all peak traffic values and perform the required analysis.

Tasks:
    - Find all peak elements
    - Calculate sum of peak values
    - Calculate product of peak values
    - Find maximum peak value

Input:
    A list of integers.

Output:
    Peaks, Sum, Product, Maximum Peak

Test Cases:
    Input : [10, 50, 30, 70, 60, 90, 80]
    Output:
        Peaks = [50, 70, 90]
        Sum = 210
        Product = 315000
        Max Peak = 90

    Input : [100, 200, 150, 180, 170]
    Output:
        Peaks = [200, 180]
        Sum = 380
        Product = 36000
        Max Peak = 200

    Input : [5]
    Output:
        Peaks = [5]
        Sum = 5
        Product = 5
        Max Peak = 5
"""

arr = list(map(int, input("Enter numbers: ").split(",")))

peaks = []

for i in range(len(arr)):
    if i == 0:
        if len(arr) == 1 or arr[i] >= arr[i + 1]:
            peaks.append(arr[i])
            print(f"Peak Element: {arr[i]} at Index {i}")

    elif i == len(arr) - 1:
        if arr[i] >= arr[i - 1]:
            peaks.append(arr[i])
            print(f"Peak Element: {arr[i]} at Index {i}")

    else:
        if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
            peaks.append(arr[i])
            print(f"Peak Element: {arr[i]} at Index {i}")

print("Peak Elements:", peaks)
sum=0
prod=1
max=peaks[0]

for i in peaks:
    sum+=i
    prod*=i
    if i>max:
        max=i

print(f"Sum Of Peaks : {sum}")
print(f"product Of Peaks : {prod}")
print(f"max Of Peaks : {max}")