"""
7.

A cricket academy wants to analyze player performance. Each player's information is stored as a tuple.

Tuple Format:

(player_id, player_name, runs_scored)

Requirements:

Read N player records from the user and store them as tuples in a list.
Display all player records.
Find and display the player who scored the highest runs.
Find and display the player who scored the lowest runs.
Calculate and display the total runs scored by all players.
Calculate and display the average runs scored.
Display players who scored more than 50 runs.

Test Case:

Input:

Enter number of players: 5

101 Virat 82
102 Rohit 45
103 Gill 120
104 Hardik 38
105 SKY 76

Expected Output:

All Players:
(101, 'Virat', 82)
(102, 'Rohit', 45)
(103, 'Gill', 120)
(104, 'Hardik', 38)
(105, 'SKY', 76)

Highest Scorer:
(103, 'Gill', 120)

Lowest Scorer:
(104, 'Hardik', 38)

Total Runs:
361

Average Runs:
72.2

Players Scoring More Than 50 Runs:
(101, 'Virat', 82)
(103, 'Gill', 120)
(105, 'SKY', 76)
"""
n=int(input("Enter The Number of Players : "))
list=[]


for i in range(n):
    print(f"Enter Player {i+1} Details")
    id=int(input("Enter Player ID       : "))
    name=input("Enter Player Name     : ")
    runs=int(input("Enter Runs Scored     : "))

    player=(id,name,runs)
    list.append(player)

    print(f"{i+1}th Player Details Stored ...")
    print()


print("All Player Details : ")

for i in list:
    print(i)


highest=list[0]
lowest=list[0]
total=0

for i in list:
    if i[2]>highest[2]:
        highest=i

    if i[2]<lowest[2]:
        lowest=i

    total+=i[2]


print("Highest Scorer : ")
print(highest)


print("Lowest Scorer : ")
print(lowest)


print(f"Total Runs : {total}")


print(f"Average Runs : {total/n}")


print("Players Scoring More Than 50 Runs : ")

for i in list:
    if i[2]>50:
        print(i)