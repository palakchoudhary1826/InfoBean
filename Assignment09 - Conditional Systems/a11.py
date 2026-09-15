'''
Docstring for Assignment09.a11
Airline Ticket Pricing Engine

An airline calculates ticket price based on class, distance, and booking time.

If class is business, then check distance. If distance is greater than 1000, price is 8000; otherwise 5000.

If class is economy, then check distance. If distance is greater than 1000, then check booking time. If booking is early, price is 4000; otherwise 5000. If distance is less than or equal to 1000, price is 2500.

Input:
Class = economy
Distance = 1200
Booking = early

Output:
Ticket Price = 4000
'''
travel_class = input("Enter Class (business/economy): ").lower()
distance = int(input("Enter Distance (in km): "))
booking_time = input("Enter Booking Time (early/late): ").lower()
p=0
if travel_class=="business":
    if distance>1000:
        p=8000
    else:
        p=5000
else:
    if distance>1000:
        if booking_time=="early":
            p=4000
        else:p=5000
    else:
        p=2500

print(f"Ticket Price :{p}")