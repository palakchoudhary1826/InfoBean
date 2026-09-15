'''
. Weather Monitoring System
   A system checks weather conditions:

* If temperature ≥ 30 → Hot day
* If humidity ≥ 70 → High humidity alert

Input:
Enter temperature: 32
Enter humidity: 75

Output:
Hot day
High humidity alert

'''
temperature=int(input("Enter The Temperature : "))
humidity=int(input("Enter The Humidity : "))

if temperature>=30:
    print("hot day")
    if humidity>=70:
        print("high humidity alert")