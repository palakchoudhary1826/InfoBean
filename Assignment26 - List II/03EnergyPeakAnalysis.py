"""
Question 3: Industrial Sensor Peak Energy Monitoring System

Problem:
    Find all peak energy values and perform the required analysis.

Tasks:
    - Find all peak values
    - Compute sum of squares
    - Compute average
    - Find difference between maximum and minimum peak

Input:
    A list of integers.

Output:
    Peaks, Sum of Squares, Average, Difference

Test Cases:
    Input : [20, 40, 30, 60, 50]
    Output:
        Peaks = [40, 60]
        Sum of Squares = 5200
        Average = 50
        Difference = 20

    Input : [10, 20, 15, 25, 20, 30]
    Output:
        Peaks = [20, 25, 30]
        Sum of Squares = 1525
        Average = 25
        Difference = 10

    Input : [5]
    Output:
        Peaks = [5]
        Sum of Squares = 25
        Average = 5
        Difference = 0
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
sqOfSum=0
max=peaks[0]
min=peaks[0]

for i in peaks:
    sum+=i
    sqOfSum+=(i**2)
    if i>max:
        max=i
    if i<min:
        min=i
    
avg=sum/len(peaks)

print(f"Square Sum Of Peaks     : {sqOfSum}")
print(f"Max Of Peaks            : {max}")
print(f"Min Of Peaks            : {min}")
print(f"Average Of Peaks        : {avg}")
print(f"Difference Of max & min : {abs(max-min)}")


