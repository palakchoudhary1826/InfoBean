# Hospital Management System — Test Cases

## Test Case 1 — Add Patient

### Input

```text
Enter choice: 1

Patient ID: 101
Patient Name: Rahul Sharma
Age: 25
Gender: Male
Disease: Fever
Mobile Number: 9876543210
```

### Expected Output

```text
Patient Added Successfully
Patient ID: 101
```

---

## Test Case 2 — Add Second Patient

### Input

```text
Enter choice: 1

Patient ID: 102
Patient Name: Priya Singh
Age: 30
Gender: Female
Disease: Migraine
Mobile Number: 9123456780
```

### Expected Output

```text
Patient Added Successfully
Patient ID: 102
```

---

## Test Case 3 — Display Patients

### Input

```text
Enter choice: 2
```

### Expected Output

```text
========== ALL PATIENTS ==========

Patient ID : 101
Name       : Rahul Sharma
Age        : 25
Gender     : Male
Disease    : Fever
Mobile     : 9876543210

Patient ID : 102
Name       : Priya Singh
Age        : 30
Gender     : Female
Disease    : Migraine
Mobile     : 9123456780

Total Patients : 2
========== END OF LIST ==========
```

---

## Test Case 4 — Search Existing Patient

### Input

```text
Enter choice: 3

Enter Patient ID: 101
```

### Expected Output

```text
========== PATIENT FOUND ==========

Patient ID : 101
Name       : Rahul Sharma
Age        : 25
Gender     : Male
Disease    : Fever
Mobile     : 9876543210

===================================
```

---

## Test Case 5 — Search Non-Existing Patient

### Input

```text
Enter choice: 3

Enter Patient ID: 999
```

### Expected Output

```text
Patient with ID 999 not found.
```

---

## Test Case 6 — Add Doctor

### Input

```text
Enter choice: 4

Doctor ID: 201
Doctor Name: Dr. Amit Verma
Specialization: Cardiologist
Experience: 8
Consultation Fees: 800
```

### Expected Output

```text
Doctor Added Successfully
Doctor ID: 201
```

---

## Test Case 7 — Add Second Doctor

### Input

```text
Enter choice: 4

Doctor ID: 202
Doctor Name: Dr. Neha Sharma
Specialization: Neurologist
Experience: 5
Consultation Fees: 1000
```

### Expected Output

```text
Doctor Added Successfully
Doctor ID: 202
```

---

## Test Case 8 — Display Doctors

### Input

```text
Enter choice: 5
```

### Expected Output

```text
========== ALL DOCTORS ==========

Doctor ID      : 201
Doctor Name    : Dr. Amit Verma
Specialization : Cardiologist
Experience     : 8 Years
Consultation   : ₹800

Doctor ID      : 202
Doctor Name    : Dr. Neha Sharma
Specialization : Neurologist
Experience     : 5 Years
Consultation   : ₹1000

Total Doctors : 2
========== END OF LIST ==========
```

---

## Test Case 9 — Book Appointment

### Input

```text
Enter choice: 6

Appointment ID: 1001
Patient ID: 101
Doctor ID: 201
Appointment Date: 15-09-2026
Appointment Time: 10:30
```

### Expected Output

```text
Appointment Booked Successfully

Appointment ID : 1001
Patient ID     : 101
Doctor ID      : 201
Date           : 15-09-2026
Time           : 10:30
```

---

## Test Case 10 — Book Second Appointment

### Input

```text
Enter choice: 6

Appointment ID: 1002
Patient ID: 102
Doctor ID: 202
Appointment Date: 16-09-2026
Appointment Time: 14:00
```

### Expected Output

```text
Appointment Booked Successfully
Appointment ID : 1002
```

---

## Test Case 11 — Show Appointments

### Input

```text
Enter choice: 7
```

### Expected Output

```text
========== ALL APPOINTMENTS ==========

Appointment ID : 1001
Patient ID     : 101
Doctor ID      : 201
Date           : 15-09-2026
Time           : 10:30

Appointment ID : 1002
Patient ID     : 102
Doctor ID      : 202
Date           : 16-09-2026
Time           : 14:00

Total Appointments : 2
========== END OF APPOINTMENTS ==========
```

---

## Test Case 12 — Generate Bill

### Input

```text
Enter choice: 8

Patient ID: 101
Consultation Charges: 800
Medicine Cost: 1200
Test Charges: 500
```

### Calculation

```text
Total Bill = 800 + 1200 + 500
Total Bill = 2500
```

### Expected Output

```text
========== PATIENT BILL ==========

Patient ID          : 101
----------------------------------
Consultation Cost   : ₹800
Medicine Cost       : ₹1200
Test Cost           : ₹500
----------------------------------
Total Bill          : ₹2500

========== END OF BILL ===========
```

---

## Test Case 13 — Generate Second Bill

### Input

```text
Enter choice: 8

Patient ID: 102
Consultation Charges: 1000
Medicine Cost: 1500
Test Charges: 750
```

### Expected Output

```text
========== PATIENT BILL ==========

Patient ID          : 102
----------------------------------
Consultation Cost   : ₹1000
Medicine Cost       : ₹1500
Test Cost           : ₹750
----------------------------------
Total Bill          : ₹3250

========== END OF BILL ===========
```

---

## Test Case 14 — Empty Patient List

### Input

Start the program fresh and select:

```text
Enter choice: 2
```

### Expected Output

```text
========== ALL PATIENTS ==========

No patients found.
```

---

## Test Case 15 — Empty Appointment List

### Input

Start the program fresh and select:

```text
Enter choice: 7
```

### Expected Output

```text
========== ALL APPOINTMENTS ==========

No appointments found.
```

---

## Test Case 16 — Exit

### Input

```text
Enter choice: 9
```

### Expected Output

```text
Thank you for using Hospital Management System.
Program Exited Successfully.
```

---

