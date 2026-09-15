'''
Docstring for Assignment09.a17
Military Recruitment Fitness System

Selection is based on age, BMI, running time, and medical condition.

If age is between 18 and 25, then check BMI. If BMI is between 18 and 25, then check running time. If running time is less than or equal to 15 minutes, then check medical. If medical is fit, select; otherwise medical reject. If running time is more than 15, physical fail. If BMI is not in range, BMI fail.

If age is between 26 and 30, then check running time and medical. If running time is less than or equal to 14 and medical is fit, conditional selection; otherwise reject.

If age is above 30 or below 18, not eligible.

Input:
Age = 23
BMI = 22
Running Time = 14
Medical = fit

Output:
Selection Status = Selected
'''
age = int(input("Enter Age: "))
bmi = float(input("Enter BMI: "))
running_time = int(input("Enter Running Time (in minutes): "))
medical = input("Enter Medical Status (fit/unfit): ").lower()
r=""
if age>=18 and age<=25:
    if bmi>=18 and bmi<=25:
        if running_time<=15:
            if medical=="fit":
                r="select"
            else:
                r="reject"
        else:
            r="Physical fail"
    else:
        r="BMI Fail"
elif age>=26 and age<=30:
    if running_time<=14 and medical=="fit":
        r="Conditional Selection"
    else:
        r="reject"

else:
    if age>30 or age<18:
        r="not eligible"

print(f"Selection Status : {r}")
