'''
8. Weather Monitoring System

A weather monitoring system classifies the weather condition based on temperature:

* Below 0°C → Freezing
* 0°C to 20°C → Cold
* 21°C to 35°C → Warm
* Above 35°C → Hot

Write a Python program to classify the weather.

Input:
Enter temperature: 38

Output:
Weather Condition: Hot

'''
t=int(input("Enter The Temperature : "))

if t==0:
    print("weather condition : freezing")
elif t<=20:
    print("weather condition : cold")
elif t<=35:
    print("Weather condition : warm")
    
else:
    print("weather condition : hot")