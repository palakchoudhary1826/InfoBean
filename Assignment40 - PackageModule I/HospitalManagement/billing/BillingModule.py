def generateBill():
    pId = int(input("Enter Patient Id : "))
    ConsultCost = int(input("Enter Consultation Cost : "))
    medCost = int(input("Enter Medicine Cost : "))
    testCost = int(input("Enter Test Cost :"))

    totalBill = ConsultCost + medCost + testCost

    print("========== PATIENT BILL ==========")
    print(f"Patient ID          : {pId}")
    print("----------------------------------")
    print(f"Consultation Cost   : ₹{ConsultCost}")
    print(f"Medicine Cost       : ₹{medCost}")
    print(f"Test Cost           : ₹{testCost}")
    print("----------------------------------")
    print(f"Total Bill          : ₹{totalBill}")
    print("========== END OF BILL ===========")