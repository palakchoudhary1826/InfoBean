# Assignment — Hospital Management System Using Python Packages and Modules

## Problem Statement

Develop a **menu-driven Hospital Management System** application in Python.

The application should be developed using proper **packages and modules**.

**Do not write the complete program in a single file.** Divide the application into different packages based on functionality.

---

# Project Structure

```text
HospitalManagement/

    01Main.py

    patient/
        __init__.py
        02PatientModule.py

    doctor/
        __init__.py
        03DoctorModule.py

    appointment/
        __init__.py
        04AppointmentModule.py

    billing/
        __init__.py
        05BillingModule.py
```

---

# 1. Patient Management Package

Create a package named:

```text
patient
```

Create the module:

```text
02PatientModule.py
```

Implement the following functions.

## a) `add_patient()`

Take the following patient details from the user:

* Patient ID
* Patient Name
* Age
* Gender
* Disease
* Mobile Number

Store patient information using:

* List
* Dictionary

## b) `display_patients()`

Display all registered patients.

## c) `search_patient()`

Search for patient details using **Patient ID**.

---

# 2. Doctor Management Package

Create a package named:

```text
doctor
```

Create the module:

```text
03DoctorModule.py
```

Implement the following functions.

## a) `add_doctor()`

Take the following doctor details from the user:

* Doctor ID
* Doctor Name
* Specialization
* Experience
* Consultation Fees

Store doctor information using:

* List
* Dictionary

## b) `display_doctors()`

Display all doctor details.

---

# 3. Appointment Management Package

Create a package named:

```text
appointment
```

Create the module:

```text
04AppointmentModule.py
```

Implement the following functions.

## a) `book_appointment()`

Take the following appointment details from the user:

* Appointment ID
* Patient ID
* Doctor ID
* Appointment Date
* Appointment Time

Store appointment information using a list and dictionary.

## b) `show_appointments()`

Display all booked appointments.

---

# 4. Billing Package

Create a package named:

```text
billing
```

Create the module:

```text
05BillingModule.py
```

Implement the following function.

## `generate_bill()`

Take the following details from the user:

* Patient ID
* Consultation Charges
* Medicine Cost
* Test Charges

Calculate the total bill:

```text
Total Bill = Consultation Charges + Medicine Cost + Test Charges
```

Display the complete bill.

---

# 5. Main Application

Create:

```text
01Main.py
```

Create a **menu-driven program**.

Display the following menu:

```text
========== Hospital Management System ==========

1. Add Patient
2. Display Patients
3. Search Patient
4. Add Doctor
5. Display Doctors
6. Book Appointment
7. Show Appointments
8. Generate Bill
9. Exit
```

According to the user's choice, call the required functions from the appropriate packages and modules.

---

# Requirements

1. Use separate packages for:

   * Patient Management
   * Doctor Management
   * Appointment Management
   * Billing

2. Use separate modules for each functionality.

3. Use `__init__.py` inside every package.

4. Use functions for each operation.

5. Use lists and dictionaries to store records.

6. Use imports to access functions from different packages.

7. Implement the application using a menu-driven approach.

8. Do not write the entire application in a single file.

9. Use meaningful variable and function names.

10. The program should continue displaying the menu until the user selects **Exit**.

---

# Expected Learning Outcomes

After completing this assignment, you should understand:

* Python packages
* Python modules
* `__init__.py`
* Importing modules
* Importing functions from packages
* Lists
* Dictionaries
* Functions
* Menu-driven programs
* Sharing data between modules
* Organizing a Python project into multiple files
