doctorDB = []
doctorId = 100


def addDoctor():
    global doctorId

    name = input("Enter Doctor Name   : ")
    age = int(input("Enter Doctor Age : "))
    gender = input("Enter Gender (Male/Female) : ")
    specialization = input("Enter Specialization : ")
    mobNum = input("Enter The Mobile Number : ")

    doctor = {
        "d_id": doctorId,
        "d_name": name,
        "d_age": age,
        "d_gender": gender,
        "d_specialization": specialization,
        "d_mobNum": mobNum
    }

    doctorDB.append(doctor)

    print(f"Doctor Added With ID : {doctorId}")

    doctorId += 1


def displayDoctor():

    print("========== ALL DOCTORS ==========")

    if not doctorDB:
        print("No doctors found.")
        return

    for doctor in doctorDB:

        print("----------------------------------")
        print(f"Doctor ID    : {doctor['d_id']}")
        print(f"Name         : {doctor['d_name']}")
        print(f"Age          : {doctor['d_age']}")
        print(f"Gender       : {doctor['d_gender']}")
        print(f"Specialization : {doctor['d_specialization']}")
        print(f"Mobile       : {doctor['d_mobNum']}")

    print("----------------------------------")
    print(f"Total Doctors : {len(doctorDB)}")
    print("========== END OF LIST ==========")