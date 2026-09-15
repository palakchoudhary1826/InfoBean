'''

4. A gym provides personalized plans based on age, weight, and fitness goal.
The system should take age, weight, and goal (weight loss or muscle gain) as input.
 If the age is greater than or equal to 18, then check the weight. If the weight is greater than or equal to 80, then check the goal. If the goal is "weight loss", assign "Cardio Plan"; otherwise, assign
"Strength Plan". If the weight is less than 80, assign "General Fitness Plan". If the age is less than 18, display
 "Not Allowed". Display the recommended plan.

Input:
Age = 25
Weight = 85
Goal = weight loss

Output:
Plan = Cardio Plan

'''

age=int(input("Enter The Age : "))
weight= int(input("Enter The Weight : "))
goal=input("Enter The Fitness Goal(weight loss or muscle gain) : ").lower()

assign=""

if age>=18:
    if weight>=80:
        if goal=="weight loss":
            assign="Cardio Plan"
        else:
            assign="Strength Plan"
    else:
        assign="General Fitness Plan"
        
        
else:
    assign="Not Allowed "
        
        

print(f"Plan : {assign}")