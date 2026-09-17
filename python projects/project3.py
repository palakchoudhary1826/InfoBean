

username = "student"
password = "1234"

attempt = 3

while attempt > 0:
    user = input("Enter Username: ")
    pwd = input("Enter Password: ")

    if user == username and pwd == password:
        print("✅ Login Successful")
        break
    else:
        attempt -= 1
        print("❌ Invalid Username or Password")
        print("Attempts Left:", attempt)

if attempt == 0:
    print("🚫 Account Locked!")
    exit()


name = ""
roll = ""
branch = ""
year = ""
mobile = ""
email = ""
total_class=80
attendance = 0

percentage = 0
grade = ""
fee_status = ""
remaining_fee = 0
scholarship = ""


while True:

    print("\n===================================")
    print("     STUDENT MANAGEMENT SYSTEM")
    print("===================================")
    print("1. Student Profile")
    print("2. Attendance")
    print("3. Marks")
    print("4. Fee Details")
    print("5. Scholarship")
    print("6. Dashboard")
    print("7. Logout")

    choice = input("Enter Your Choice: ")

    
    if choice == "1":

        print("\n------ Student Profile ------")

        name = input("Enter Name : ")
        roll = input("Enter Roll Number : ")
        branch = input("Enter Branch : ")
        year = input("Enter Year : ")
        mobile = input("Enter Mobile Number : ")
        email = input("Enter Email : ")

        print("\nProfile Saved Successfully ✅")

    
    elif choice == "2":

        print("\n------ Attendance ------")

        print("your total class is ",total_class)
        attended = int(input("Enter Attended Classes : "))

        attendance = (attended / total_class) * 100

        print("Attendance =", attendance, "%")

        if attendance >= 75:
            print( name,"✅ your Eligible For Exam")
        else:
            print("❌your Not Eligible For Exam")

    

    
    elif choice == "3":

     print("\n------ Marks ------")

     m1 = int(input("Enter Marks of Subject 1: "))
     m2 = int(input("Enter Marks of Subject 2: "))
     m3 = int(input("Enter Marks of Subject 3: "))
     m4 = int(input("Enter Marks of Subject 4: "))
     m5 = int(input("Enter Marks of Subject 5: "))

     total_marks = m1 + m2 + m3 + m4 + m5
     percentage = total_marks / 5

     print("Total Marks :", total_marks)
     print("Percentage :", percentage)

     if percentage >= 90:
            grade = "A+"
     elif percentage >= 80:
            grade = "A"
     elif percentage >= 70:
            grade = "B"
     elif percentage >= 60:
            grade = "C"
     else:
            grade = "Fail"

     print("Grade :", grade)

    
    elif choice == "4":

        print("\n------ Fee Details ------")

        total_fee = int(input("Enter Total Fee : "))
        paid_fee = int(input("Enter Paid Fee : "))

        remaining_fee = total_fee - paid_fee

        print("Remaining Fee :", remaining_fee)

        if remaining_fee == 0:
            fee_status = "Paid"
        else:
            fee_status = "Pending"

        print("Fee Status :", fee_status)

    
    elif choice == "5":

        print("\n------ Scholarship ------")

        if percentage >= 90:
            scholarship = "₹20,000"
        elif percentage >= 80:
            scholarship = "₹10,000"
        elif percentage >= 70:
            scholarship = "₹5,000"
        else:
            scholarship = "Not Eligible ,your percentage is not enough for scholorship"

        print("Scholarship :", scholarship)

    
    elif choice == "6":

        print("\n========== STUDENT DASHBOARD ==========")

        print("Name          :", name)
        print("Roll Number   :", roll)
        print("Branch        :", branch)
        print("Year          :", year)
        print("Mobile        :", mobile)
        print("Email         :", email)

        print("--------------------------------------")

        print("Attendance    :", attendance, "%")
        print("Percentage    :", percentage)
        print("Grade         :", grade)

        print("--------------------------------------")

        print("Fee Status    :", fee_status)
        print("Remaining Fee :", remaining_fee)

        print("--------------------------------------")

        print("Scholarship   :", scholarship)

        print("======================================")

    
    elif choice == "7":

        print("\nThank You", name)
        print("Logout Successfully 😊")
        break

    else:
        print("Invalid Choice")