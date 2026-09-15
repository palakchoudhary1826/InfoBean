'''

Assignment 10: Time Conversion

Convert total seconds into hours, minutes, and seconds.

Input:
Total seconds = 7384

Expected Output:
Hours = 2
Minutes = 3
Seconds = 4
'''

totalSec=int(input("Enter The Seconds : "))
hrs=totalSec//3600
r1=totalSec%3600
min=r1//60
r2=r1%60

print(f"Hours : {hrs}\nMinutes : {min}\nSeconds : {r2}")