from patient.PatientModule import addPatient,displayPatient,searchPatient
from doctor.DoctorModule import addDoctor,displayDoctor
from appointment.AppointmentModule import bookAppointment,displayAppointment
from billing.BillingModule import generateBill


def display():
    print('''========== Hospital Management System ==========

1. Add Patient
2. Display Patients
3. Search Patient
4. Add Doctor
5. Display Doctors
6. Book Appointment
7. Show Appointments
8. Generate Bill
9. Exit''')

while True:
    display()
    choice=int(input("Enter The Choice : "))

    match choice:
        case 1:
            print("Add Patient ")
            addPatient()
        case 2:
            print("Display Patient")
            displayPatient()
        case 3:
            print("Search Patient")
            searchPatient()
        case 4:
            print("Add Doctor")
            addDoctor()
        case 5:
            print("Display Doctor")
            displayDoctor()
        case 6:
            print("Book Appointment")
            bookAppointment()
        case 7:
            print("Display Appointment")
            displayAppointment()
        case 8:
            generateBill()
        case 9:
            print("Thanks For Using System")
            print("Existing ...")
        case _:
            print("Invalid Choice")
