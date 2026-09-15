def display():
    print("""
=====================================
   HOSPITAL PATIENT MANAGEMENT SYSTEM
=====================================

Menu Below

1. Add New Patient
2. Search Patient
3. Update Patient Disease
4. Delete Patient Record
5. Display All Patients
6. Count Total Patients
7. Display Patients By Disease
8. Display Oldest Patient
9. Display Youngest Patient
10. Exit
""")


def add(id):
    if id not in d:
        name = input("Enter The Patient Name : ")
        age = int(input("Enter The Patient Age : "))
        disease = input("Enter The Disease : ")
        doctor = input("Enter The Doctor : ")
        d[id] = {"name": name, "age": age, "disease": disease, "doctor": doctor}
        print(f"Patient Added SuccessFully At ID : {id}")

    else:
        print("Patient ID Already Exist")
        print(d[id])


def search(id):
    if userId in d:
        print()
        print("Patient ID :", userId)
        print("Name       :", d[userId]["name"])
        print("Age        :", d[userId]["age"])
        print("Disease    :", d[userId]["disease"])
        print("Doctor     :", d[userId]["doctor"])

    else:
        print("Patient Record Not Found")


def update(id):

    if id in d:
        newDisease = input("Enter The New Disease : ")
        d[id]["disease"] = newDisease
        print("Disease Updated ...")
    else:
        print("Patient Record Not Found")


def delete(id):

    if id in d:
        d.pop(id)
        print("Patient Removed SuccessFully ... ")
    else:
        print("Patient Not Found")


def displayPatient():

    for i in d:

        print()
        print("-" * 30)
        print("Patient ID :", i)
        print("Name       :", d[i]["name"])
        print("Age        :", d[i]["age"])
        print("Disease    :", d[i]["disease"])
        print("Doctor     :", d[i]["doctor"])
        print("-" * 30)


def findDiseaseInPatient(dis):
    found=False

    for i in d:
        if d[i]["disease"] == dis:
            print(f"{d[i]} --> {d[i]["name"]}")
            found=True
    
    if not found:
        print("Patient Not Found")


def oldAge():
    old = 0
    id = 0

    for i in d:
        age = d[i]["age"]

        if age > old:
            old = age
            id = i
    print("Oldest Patient Details")
    print(f"Patient ID : {id}")
    print(f"Patient Name : {d[id]["name"]}")
    print(f"Age : {d[id]["age"]}")
    print(f"Disease : {d[id]["disease"]}")
    print(f"Doctor : {d[id]["doctor"]}")


def youngAge():
    if not d:
        print("No Patient Found")
        return
    
    young = d[0]["age"]
    id = 0

    for i in d:
        age = d[i]["age"]

        if age < young:
            young = age
            id = i
    print("Youngest Patient Details")
    print(f"Patient ID : {id}")
    print(f"Patient Name : {d[id]["name"]}")
    print(f"Age : {d[id]["age"]}")
    print(f"Disease : {d[id]["disease"]}")
    print(f"Doctor : {d[id]["doctor"]}")


d = {}  # dict
id = 100


while True:
    display()
    choice = int(input("Enter The Option : "))

    match choice:
        case 1:
            print("ADD NEW PATIENT")

            # id = input("Enter The Patient ID : ")
            id += 1
            add(id)

        case 2:
            print("Search Patient ")

            userId = int(input("Enter The ID : "))
            search(userId)

        case 3:
            print("Update Patient Disease")

            userId = int(input("Enter The ID : "))
            update(userId)

        case 4:
            print("Delete Patient Record")
            userId = int(input("Enter The ID : "))
            delete(userId)

        case 5:
            print("Display All Patients")
            displayPatient()

        case 6:
            print("Count Total Patients")
            print(f"Total Patients : {len(d)}")

        case 7:
            print("Display Patietns By Disease")
            userDisease = input("Enter The Disease : ")
            findDiseaseInPatient(userDisease)

        case 8:
            print("Display Oldest Patient")

            oldAge()

        case 9:
            print("Display Young Patient")

            youngAge()

        case 10:
            print("Thank You For Using Hosptital Patient Management System")
            break

        case _:
            print("Invalid Choice")
