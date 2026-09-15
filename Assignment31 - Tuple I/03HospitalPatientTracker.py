"""
QUESTION 3: HOSPITAL PATIENT TRACKER

A hospital stores patient records for daily monitoring.

Fields:
patient_id, patient_name, age, disease

Requirements:

1. Read N patient records from the user and store them in a list of NamedTuples.

2. Display all patient details.

3. Display patients whose age is above 60 years.

4. Search for a patient using Patient ID.

5. Count the number of patients suffering from a particular disease.

Test Case:

Input:
Enter number of patients: 4

P101 Rajesh 65 Diabetes
P102 Suman 45 Fever
P103 Mohan 70 Diabetes
P104 Rita 35 Cold

Enter Patient ID: P103
Enter Disease: Diabetes

Expected Output:
Patient Found:
P103 Mohan 70 Diabetes

Patients Above 60:
P101 Rajesh 65 Diabetes
P103 Mohan 70 Diabetes

Patients with Diabetes:
2
"""


from collections import namedtuple


patient=namedtuple("patient",["patient_id","patient_name","age","disease"])


n=int(input("Enter The Number of Patients : "))
list=[]


for i in range(n):
    print(f"Enter Patient {i+1} Details")
    id=input("Enter Patient ID       : ")
    name=input("Enter Patient Name     : ")
    age=input("Enter Age              : ")
    disease=input("Enter Disease          : ")
    list.append(patient(id,name,int(age),disease))
    print(f"{i+1}th Patient Details Stored ...")
    print()


print(list)


print("All Patient Details : ")


count=1


for i in list:
    print(f"{count}th Patient Details")
    print(f"Patient ID   : {i.patient_id}")
    print(f"Name         : {i.patient_name}")
    print(f"Age          : {i.age}")
    print(f"Disease      : {i.disease}")
    count+=1
    print()


print("Patients Above 60 : ")

for i in list:
    if i.age>60:
        print(f"Patient ID   : {i.patient_id}")
        print(f"Name         : {i.patient_name}")
        print(f"Age          : {i.age}")
        print(f"Disease      : {i.disease}")
        print()


id=input("Enter Patient ID : ")

found=False

for i in list:
    if i.patient_id==id:
        print("\nPatient Found : ")
        print(f"Patient ID   : {i.patient_id}")
        print(f"Name         : {i.patient_name}")
        print(f"Age          : {i.age}")
        print(f"Disease      : {i.disease}")
        found=True

if found==False:
    print("\nPatient Not Found")


disease=input("\nEnter Disease : ")

count=0

for i in list:
    if i.disease==disease:
        count+=1


print(f"\nPatients with {disease} : {count}")