'''
Assignment 4: Travel Distance Calculation

A person is traveling at a constant speed. Time is given in hours and minutes. Convert total time into hours and calculate distance.

Input:
Speed = 60 km/hr
Time = 2 hours 30 minutes

Expected Output:
Total Time = 2.5 hours
Distance = 150.0 km

'''

speed=int(input("Enter The Speed :- "))
tHrs,tMin=map(int,input("Enter The hrs then min :- ").split())

print(f"Speed : {speed}km/hrs")
print(f"Time : {tHrs} hours {tMin} Minutes")

minTohrs=tMin/60;
totalTime=tHrs+minTohrs;
print(f"TotalTime :{totalTime} hours")
print(f"Distance :{speed*totalTime} km")
