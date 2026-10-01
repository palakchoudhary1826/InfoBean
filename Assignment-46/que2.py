from abc import ABC, abstractmethod

class Patient(ABC):

    def __init__(self, patient_id, patient_name, patient_age,
                 number_of_days, medicine_charge):

        self.patient_id = patient_id
        self.patient_name = patient_name
        self.patient_age = patient_age
        self.number_of_days = number_of_days
        self.medicine_charge = medicine_charge

        self.consultation_fee = 0
        self.room_charges = 0
        self.total_bill = 0
        self.discount = 0
        self.final_amount = 0
        self.bill_status = "NOT GENERATED"

    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def calculate_discount(self):
        pass

    @abstractmethod
    def calculate_final_amount(self):
        pass

    @abstractmethod
    def generate_bill(self):
        pass

class GeneralPatient(Patient):

    def calculate_bill(self):

        self.consultation_fee = 500
        self.room_charges = self.number_of_days * 1000

        self.total_bill = (
            self.consultation_fee
            + self.room_charges
            + self.medicine_charge
        )

    def calculate_discount(self):

        self.discount = 0

    def calculate_final_amount(self):

        self.final_amount = self.total_bill - self.discount

    def generate_bill(self):

        self.calculate_bill()
        self.calculate_discount()
        self.calculate_final_amount()

        self.bill_status = "GENERATED"

        print("\n========================================")
        print("            PATIENT BILL")
        print("========================================")

        print(f"Patient ID       : {self.patient_id}")
        print(f"Patient Name     : {self.patient_name}")
        print(f"Patient Age      : {self.patient_age}")
        print("Patient Type     : General")

        print("\nConsultation Fee : Rs.{:.2f}".format(
            self.consultation_fee
        ))

        print("Room Charges     : Rs.{:.2f}".format(
            self.room_charges
        ))

        print("Medicine Charges : Rs.{:.2f}".format(
            self.medicine_charge
        ))

        print("\n----------------------------------------")

        print("Total Hospital Bill : Rs.{:.2f}".format(
            self.total_bill
        ))

        print("Discount            : Rs.{:.2f}".format(
            self.discount
        ))

        print("Patient Payable     : Rs.{:.2f}".format(
            self.final_amount
        ))

        print("\nBill Status         :", self.bill_status)

        print("========================================")

class EmergencyPatient(Patient):

    def calculate_bill(self):

        self.consultation_fee = 1000
        emergency_charge = 500

        self.room_charges = self.number_of_days * 2000

        self.total_bill = (
            self.consultation_fee
            + emergency_charge
            + self.room_charges
            + self.medicine_charge
        )

    def calculate_discount(self):

        self.discount = 0

    def calculate_final_amount(self):

        self.final_amount = self.total_bill - self.discount

    def generate_bill(self):

        self.calculate_bill()
        self.calculate_discount()
        self.calculate_final_amount()

        self.bill_status = "GENERATED"

        print("\n========================================")
        print("            PATIENT BILL")
        print("========================================")

        print(f"Patient ID       : {self.patient_id}")
        print(f"Patient Name     : {self.patient_name}")
        print(f"Patient Age      : {self.patient_age}")
        print("Patient Type     : Emergency")

        print("\nConsultation Fee : Rs.{:.2f}".format(
            self.consultation_fee
        ))

        print("Emergency Charge : Rs.500.00")

        print("Room Charges     : Rs.{:.2f}".format(
            self.room_charges
        ))

        print("Medicine Charges : Rs.{:.2f}".format(
            self.medicine_charge
        ))

        print("\n----------------------------------------")

        print("Total Hospital Bill : Rs.{:.2f}".format(
            self.total_bill
        ))

        print("Discount            : Rs.{:.2f}".format(
            self.discount
        ))

        print("Patient Payable     : Rs.{:.2f}".format(
            self.final_amount
        ))

        print("\nBill Status         :", self.bill_status)

        print("========================================")


class InsurancePatient(Patient):

    def calculate_bill(self):

        self.consultation_fee = 800
        self.room_charges = self.number_of_days * 1500

        self.total_bill = (
            self.consultation_fee
            + self.room_charges
            + self.medicine_charge
        )

    def calculate_discount(self):

        self.discount = self.total_bill * 0.70

    def calculate_final_amount(self):

        self.final_amount = self.total_bill - self.discount

    def generate_bill(self):

        self.calculate_bill()
        self.calculate_discount()
        self.calculate_final_amount()

        self.bill_status = "GENERATED"

        print("\n========================================")
        print("            PATIENT BILL")
        print("========================================")

        print(f"Patient ID       : {self.patient_id}")
        print(f"Patient Name     : {self.patient_name}")
        print(f"Patient Age      : {self.patient_age}")
        print("Patient Type     : Insurance")

        print("\nConsultation Fee : Rs.{:.2f}".format(
            self.consultation_fee
        ))

        print("Room Charges     : Rs.{:.2f}".format(
            self.room_charges
        ))

        print("Medicine Charges : Rs.{:.2f}".format(
            self.medicine_charge
        ))

        print("\n----------------------------------------")

        print("Total Hospital Bill : Rs.{:.2f}".format(
            self.total_bill
        ))

        print("Insurance Coverage  : 70%")

        print("Insurance Amount    : Rs.{:.2f}".format(
            self.discount
        ))

        print("\nPatient Payable     : Rs.{:.2f}".format(
            self.final_amount
        ))

        print("\nBill Status         :", self.bill_status)

        print("========================================")


class CorporatePatient(Patient):

    def calculate_bill(self):

        self.consultation_fee = 700
        self.room_charges = self.number_of_days * 1200

        self.total_bill = (
            self.consultation_fee
            + self.room_charges
            + self.medicine_charge
        )

    def calculate_discount(self):

        # Corporate discount = 20%
        self.discount = self.total_bill * 0.20

    def calculate_final_amount(self):

        self.final_amount = self.total_bill - self.discount

    def generate_bill(self):

        self.calculate_bill()
        self.calculate_discount()
        self.calculate_final_amount()

        self.bill_status = "GENERATED"

        print("\n========================================")
        print("            PATIENT BILL")
        print("========================================")

        print(f"Patient ID       : {self.patient_id}")
        print(f"Patient Name     : {self.patient_name}")
        print(f"Patient Age      : {self.patient_age}")
        print("Patient Type     : Corporate")

        print("\nConsultation Fee : Rs.{:.2f}".format(
            self.consultation_fee
        ))

        print("Room Charges     : Rs.{:.2f}".format(
            self.room_charges
        ))

        print("Medicine Charges : Rs.{:.2f}".format(
            self.medicine_charge
        ))

        print("\n----------------------------------------")

        print("Total Hospital Bill : Rs.{:.2f}".format(
            self.total_bill
        ))

        print("Corporate Discount  : 20%")

        print("Discount Amount     : Rs.{:.2f}".format(
            self.discount
        ))

        print("\nPatient Payable     : Rs.{:.2f}".format(
            self.final_amount
        ))

        print("\nBill Status         :", self.bill_status)

        print("========================================")


def register_patient():

    print("\n========================================")
    print("          REGISTER PATIENT")
    print("========================================")

    patient_id = input("Enter Patient ID: ")
    patient_name = input("Enter Patient Name: ")
    patient_age = int(input("Enter Patient Age: "))

    print("\nSelect Patient Type:")
    print("1. General")
    print("2. Emergency")
    print("3. Insurance")
    print("4. Corporate")

    choice = input("\nEnter choice: ")

    number_of_days = int(input("\nEnter Number of Days: "))
    medicine_charge = float(input("Enter Medicine Charge: "))

    patient = None

    if choice == "1":

        patient = GeneralPatient(
            patient_id,
            patient_name,
            patient_age,
            number_of_days,
            medicine_charge
        )


    elif choice == "2":

        patient = EmergencyPatient(
            patient_id,
            patient_name,
            patient_age,
            number_of_days,
            medicine_charge
        )
    elif choice == "3":

        patient = InsurancePatient(
            patient_id,
            patient_name,
            patient_age,
            number_of_days,
            medicine_charge)

    elif choice == "4":

        patient = CorporatePatient(
            patient_id,
            patient_name,
            patient_age,
            number_of_days,
            medicine_charge
        )

    else:

        print("\nInvalid patient type.")
        return

    patients[patient_id] = patient

    print("\nPatient registered successfully.")


def generate_patient_bill():

    patient_id = input("\nEnter Patient ID: ")

    if patient_id in patients:

        patient = patients[patient_id]

        patient.generate_bill()

    else:

        print("\nPatient record not found.")


def view_patient_bill():

    patient_id = input("\nEnter Patient ID: ")

    if patient_id in patients:

        patient = patients[patient_id]

        if patient.bill_status == "GENERATED":
            patient.generate_bill()

        else:
            print("\nBill has not been generated yet.")

    else:

        print("\nPatient record not found.")

patients = {}


while True:

    print("\n")
    print("========================================")
    print("       HOSPITAL MANAGEMENT SYSTEM")
    print("========================================")

    print("1. Register Patient")
    print("2. Generate Patient Bill")
    print("3. View Patient Bill")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        register_patient()

    elif choice == "2":

        generate_patient_bill()

    elif choice == "3":

        view_patient_bill()
    elif choice == "4":

        print("\nThank you for using Hospital Management System.")
        break

    else:

        print("\nInvalid choice. Please try again.")