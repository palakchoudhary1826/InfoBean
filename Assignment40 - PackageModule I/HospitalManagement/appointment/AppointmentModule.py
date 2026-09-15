from datetime import date,time ,datetime
appointmentDB=[]

appointId=1000

def bookAppointment():
    global appointId
    pId=int(input("Enter The Patient ID: "))
    dId=int(input("Enter The Doctor ID : "))

    d1,m1,y1=map(int,input("Enter Appointment Date (DD-MM-YYYY)").split("-"))
    appointDate=date(y1,m1,d1)

    h1,min1=map(int,input("Enter Appointment Time (HH:MM)").split(":"))
    appointTime=time(h1,min1)

    appointment={
        "app_Id":appointId,
        "p_Id":pId,
        "d_Id":dId,
        "app_Date":appointDate,
        "app_Time":appointTime
    }

    appointmentDB.append(appointment)
    print(f"Appointment Book Successfull ID  : {appointId}")
    appointId+=10

def displayAppointment():

    print("========== ALL APPOINTMENTS ==========")

    if not appointmentDB:
        print("No appointments found.")
        return

    for appointment in appointmentDB:

        print("--------------------------------------")
        print(f"Appointment ID : {appointment['app_Id']}")
        print(f"Patient ID     : {appointment['p_Id']}")
        print(f"Doctor ID      : {appointment['d_Id']}")
        print(f"Date           : {appointment['app_Date'].strftime('%d-%m-%Y')}")
        print(f"Time           : {appointment['app_Time'].strftime('%H:%M')}")

    print("--------------------------------------")
    print(f"Total Appointments : {len(appointmentDB)}")
    print("========== END OF LIST ==========")
