while True:
    print("=========================================")
    print("==========🚨🚨SMART PUBLIC PORTAL🚨🚨==========")
    print("=========================================")
    print("1.citizen registration")
    print("2.complaint registration")
    print("3.check complaint status")
    print("4.update complaint status")
    print("5.view Reports")
    print("6.Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        print("***-------Registering citizen📝-------***")

        name=input("enter your name:")


        age=int(input("enter your age:"))
    

        mobile_number=int(input("enter your mobile number:"))
    

        city=input("enter your city:")

        confirm=input("confirm your citizen registration (yes/no):")
        if confirm.lower() == "yes":
            print("Citizen registered successfully!")
        else:
            print("Citizen registration canceled.")

    

    elif choice == "2":
        print("***-------Registering complaint🖊️-------***")
        while True:
            print("1.Road issue ")
            print("2.water issue")
            print("3.electricity issue")
            print("4.sanitation isuue")
            print("5.other issue")
            
            ch = input("Enter your choice: ")
            if ch == "1":
                road_issue=input('enter the road issue details:')
                print("road issue registered:",road_issue)
            elif ch =="2":
                water_issue=input("enter the water issue details:")
                print("water issue registered:",water_issue)
            elif ch =="3":
                electricity_issue=input("enter the electricity issue details:")
                print("electricity issue registered:",electricity_issue)    
            elif ch =="4":
                sanitation_issue=input("enter the sanitation issue details:")
                print("sanitation issue registered:",sanitation_issue)
            elif ch =="5":
                other_issue=input("enter the other issue details:")
                print("other issue registered:",other_issue)

            
            confirm=input("confirm your complaint registration (yes/no):")
            if confirm.lower() == "yes":
                print("complaint registered successfully!")
                break
            else:
               print("complaint registration canceled.")
               break
        

        

    
            
    elif choice == "3":
        print("***-------Checking complaint status🔍🔍-------***")
        while True:
            print("1.Road issue")
            print("2.water issue")
            print("3.electricity issue")
            print("4.sanitation isuue")
            print("5.other issue")
            c = input("Enter your choice: ")
            if c == "1":
              print("Road issue priority: High")
            elif c == "2":
              print("Water issue priority: Medium")
            elif c == "3":
              print("Electricity issue priority: High")
            elif c == "4":
                print("Sanitation issue priority: Medium")
            elif c == "5":
                print("Other issue priority: Low")
            break
            
                 

    elif choice == "4":
        print("***-------Updating complaint status🧾🧾-------***")
        while True:
            print("1.Road issue ")
            print("2.water issue")
            print("3.electricity issue")
            print("4.sanitation isuue")
            print("5.other issue")
            p = input("Enter your choice: ")
            if p == "1":
                print("Road issue status: Resolved")
            elif p == "2":
                print("Water issue status: In Progress")
            elif p == "3":
                print("Electricity issue status: Resolved")
            elif p == "4":
                print("Sanitation issue status: In Progress")
            elif p == "5":
                print("Other issue status: Pending")
            break
            

        
    
    elif choice == "5":
        print("***-------Viewing Reports📝📝-------***")
        total_complaints = 87
        resolved_complaints = 60
        pending_complaints = 40
        high_priority_complaints = 30
        medium_priority_complaints = 50
        low_priority_complaints = 20
        
        print(f"Total Complaints: {total_complaints}")
        print(f"Resolved Complaints: {resolved_complaints}")
        print(f"Pending Complaints: {pending_complaints}") 
        print(f"High Priority Complaints: {high_priority_complaints}")
        print(f"Medium Priority Complaints: {medium_priority_complaints}")
        print(f"Low Priority Complaints: {low_priority_complaints}")




    elif choice == "6":
        print("Exiting the program. Goodbye!❤️ 😊")
        break



        


