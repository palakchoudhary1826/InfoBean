'''

12. Restaurant Bill with GST System

A restaurant applies GST based on the total bill amount:

* Up to ₹1000 → 5% GST
* ₹1001 to ₹5000 → 12% GST
* Above ₹5000 → 18% GST
  Additionally, if the bill exceeds ₹3000, a service charge of ₹200 is added.

Write a Python program to calculate the final bill.

Input:
Enter bill amount: 4000

Output:
Final Bill Amount: ₹4680
'''

amt=int(input("Enter The Bill Amount : "))
final=0
if amt>5000:
    final=amt+(amt*18)/100+200
elif amt>=3000:
    final=amt+(amt*12)/100+200
elif amt>=1001:
    final=amt+(amt*12)/100
else:
    final=amt+(amt*5)/100
    
print(f"Final Bill Amount: {final}")


    