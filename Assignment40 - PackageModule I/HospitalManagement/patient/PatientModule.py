patientsDb=[]
id=100
def addPatient():
    global id
    name=input("Enter Patient Name   : ")
    age=int(input("Enter Patient Age : "))
    gender=input("Enter Gender (Male/Femal) : ")
    disease=input("Enter The Disease : ")
    MobNum=int(input("Enter The Mobile Number : "))
    patient={
        "p_id":id,
        "p_name":name,
        "p_age":age,
        "p_gender":gender,
        "p_disease":disease,
        "p_MobNum":MobNum
    }

    patientsDb.append(patient)
    print(f"Patient Added With ID : {id}")
    id+=1

def displayPatient():

    print("========== ALL PATIENTS ==========")

    if not patientsDb:
        print("No patients found.")
        return

    for patient in patientsDb:
        print("----------------------------------")
        print(f"Patient ID : {patient['p_id']}")
        print(f"Name       : {patient['p_name']}")
        print(f"Age        : {patient['p_age']}")
        print(f"Gender     : {patient['p_gender']}")
        print(f"Disease    : {patient['p_disease']}")
        print(f"Mobile     : {patient['p_MobNum']}")

    print("----------------------------------")
    print(f"Total Patients : {len(patientsDb)}")
    print("========== END OF LIST ==========")
    
def searchPatient():
    checkId=int(input("Enter ID Of Patient : "))

    for patient in patientsDb:
        if patient["p_id"]==checkId:
            print("----------------------------------")
            print(f"Patient ID : {patient['p_id']}")
            print(f"Name       : {patient['p_name']}")
            print(f"Age        : {patient['p_age']}")
            print(f"Gender     : {patient['p_gender']}")
            print(f"Disease    : {patient['p_disease']}")
            print(f"Mobile     : {patient['p_MobNum']}")
            print("----------------------------------")
            break
        else:
            print("Patient Not Found 🥲")




















    

