while True:
    print("==================================================")
    print(" --------CAMPUS MANAGEMENT SYSTEM---------")
    print("=====================================================")
    print("1. student login")
    print("2. Hostel Room Allocation")
    print("3. Canteen food ordering")
    print("4. Career guidance")
    print("5. Student Dashboard")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("=========Hostel Room Allocation🏡🏡=========")
        name = input("Enter your name: ")
        year = int(input("Enter your year of study: "))
        gender = input("Enter your gender (M/F): ")
        room=int(input("how many rooms you want to book:"))
        if room<10:
          print("Room allocated successfully!")
        else:
         print("Sorry, no rooms available.")
        confirm = input("Confirm your room allocation (yes/no): ")
        if confirm.lower() == "yes":    
           print("Room allocation confirmed!")
        else:
           print("Room allocation canceled.")

    elif choice == "2":
        print("=========Canteen Food Ordering🍔=========")
        print("1.Veg Thali")
        print("2.Non-Veg Thali")
        print("3.Sandwich")
        print("4.Beverages")
        food_choice = input("Enter your choice: ")
        if food_choice == "1":
            print("Veg Thali ordered successfully!,your bill is 100rs")
        elif food_choice == "2":
            print("Non-Veg Thali ordered successfully!,your bill is 150rs")
        elif food_choice == "3":
            print("Sandwich ordered successfully!,your bill is 50rs ")
        elif food_choice == "4":
            print("Beverages ordered successfully!,your bill is 20rs")
        else:
            print("Invalid choice.")
        confirm = input("Confirm your food order (yes/no): ")
        if confirm.lower() == "yes":
            print("Food order confirmed!")
        else:
            print("Food order canceled.")
        print("Thank you for using the Canteen Food Ordering System!")

    elif choice == "3":
        print("=========Career Guidance🎓🎓=========")
        cgpa=float(input("Enter your CGPA: "))
        if cgpa>=8.0:
            print("9+ google/microsoft/amazon internship opportunities available for you!")
        elif cgpa>=7.0:
            print("product based company internship opportunities available for you!")
        elif cgpa>=6.0:
            print("service based company internship opportunities available for you!")
        elif cgpa>=5.0:
            print("improve your skills to get better internship opportunities!")
        else:
            print("You need to work hard to improve your CGPA for better internship opportunities!")
        confirm = input("Confirm your career guidance session (yes/no): ")
        if confirm.lower() == "yes":
            print("Career guidance session confirmed!")
        else:
            print("Career guidance session canceled.")


    elif choice == "4":
        print("=========Student Dashboard📂=========")
        print("name:",name)
        print("year of study:",year)
        print("room allocated:",room)
        print("food ordered:",food_choice)
        print("cgpa:",cgpa)
    
    elif choice == "5":
        print("********Exiting the program. Goodbye!😊❤️**********")
        break

