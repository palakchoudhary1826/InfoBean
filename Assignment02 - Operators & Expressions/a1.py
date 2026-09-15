'''
========================================
Assignment 1: Time Converter
========================================

An event management company is developing a scheduling system. One of the key tasks is converting the duration of events from total seconds (which their sensor system records) into a more human-readable format of hours, minutes, and seconds.

Write a Python program that:
- Accepts the total event duration in seconds as input.
- Calculates how many hours, minutes, and seconds it corresponds to.
- Displays the output in the format:
  Hours: x, Minutes: y, Seconds: z

Sample Input:
Total event duration in seconds: 3672

Sample Output:
Hours: 1, Minutes: 1, Seconds: 12
'''

totalEventDuration=int(input("Enter The Total Event Duration In Secs :- "))
hrs=int(totalEventDuration/3600)
remainSec1=int(totalEventDuration%3600)
min=int(remainSec1/60)
remainSec2=int(remainSec1%60)


print(f"Hours:{hrs}, Minutes:{min}, Seconds:{remainSec2}")




