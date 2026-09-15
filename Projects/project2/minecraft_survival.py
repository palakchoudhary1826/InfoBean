
health = 100
hunger = 100
xp = 0
level = 1

wood = 0
stone = 0
coal = 0
iron = 0
gold = 0
diamond = 0
food = 0


day = 1
enemies_defeated = 0
game_over = False
win = False

# Equipment (0 = None, 1 = Wooden, 2 = Stone, 3 = Iron, 4 = Diamond)
pickaxe_level = 0
sword_level = 0
shield = 0
armor = 0


torch = 1

# Buildings (0 = None, 1 = Wood House, 2 = Stone House, 3 = Iron House, 4 = Castle)
house_level = 0
farm = 0
furnace = 0

# Achievements
ach_first_tree = 0
ach_first_pickaxe = 0
ach_diamond_hunter = 0
ach_home_builder = 0
ach_warrior = 0
ach_king = 0
ach_dragon_slayer = 0
ach_farmer = 0
ach_monster_hunter = 0

#Problem-1
print("=========================")
print("MINECRAFT SURVIVAL".ljust(5))
print("=========================")
input("Press Enter to Start")
xp = xp + 10

# Problem 2: Main Menu Loop 
while game_over == False and win == False:
    # Check Death
    if health <= 0:
        print("\nGAME OVER! You have died.")
        game_over = True
        break
        
    print("\n=========================")
    print("🌞Day:", day, "| 💓Health:", health, "| 🍗Hunger:", hunger, "| 🟢 XP:", xp, "| 🏆Level:", level)
    print("1. Gather Resources")
    print("2. Craft")
    print("3. Fight")
    print("4. Build")
    print("5. Report")
    print("6. Eat Food")
    print("7. Sleep (Next Day)")
    print("8. Exit")
    print("=========================")
    
    choice = input("Choose an action (1-8): ")
    action_taken = False
    
    if choice == "1":
        print("\n--- Gather Resources ---")
        print("1. Cut Trees")
        print("2. Mine Stone (Needs Pickaxe)")
        print("3. Mine Coal (Needs Pickaxe)")
        print("4. Mine Iron (Needs Stone Pickaxe)")
        
        print("5. Mine Diamond (Needs Diamond Pickaxe)")
        print("6. Collect Food")
        
        g_choice = input("What do you want to gather? ")
        
        if g_choice == "1":
            trees = int(input("How many trees? "))
            wood = wood + (trees * 2)
            xp = xp + (trees * 2)
            print("You gathered", trees * 2, "Wood.")
            action_taken = True
        elif g_choice == "2":
            if pickaxe_level >= 1:
                stone = stone + 3
                xp = xp + 5
                print("You mined 3 Stone.")
                action_taken = True
            else:
                print("You need at least a Wooden Pickaxe!")
        elif g_choice == "3":
            if pickaxe_level >= 1:
                coal = coal + 3
                xp = xp + 5
                print("You mined 2 Coal.")
                action_taken = True
            else:
                print("You need at least a Wooden Pickaxe!")
        elif g_choice == "4":
            if pickaxe_level >= 2:
                iron = iron + 3
                xp = xp + 10
                print("You mined 2 Iron.")
                action_taken = True
            else:
                print("You need at least a Stone Pickaxe!")
        
        elif g_choice == "5":
            if pickaxe_level >= 3:
                diamond = diamond + 3
                xp = xp + 20
                print("You mined 1 Diamond.")
                action_taken = True
            else:
                print("You need a Diamond or Iron Pickaxe!")
        elif g_choice == "6":
            food = food + 2
            xp = xp + 5
            print("You collected 2 Food.")
            action_taken = True
        else:
            print("Invalid choice.")
            
    elif choice == "2":
        print("\n--- Crafting ---")
        print("1. Wooden Pickaxe (5 Wood)")
        print("2. Stone Pickaxe (3 Wood, 5 Stone)")
        print("3. Iron Pickaxe (3 Wood, 5 Iron)")
        print("4. Diamond Pickaxe (3 Wood, 5 Diamond)")
        print("5. Wooden Sword (3 Wood)")
        print("6. Stone Sword (1 Wood, 3 Stone)")
        print("7. Iron Sword (1 Wood, 3 Iron)")
        print("8. Diamond Sword (1 Wood, 3 Diamond)")
        print("9. Shield (5 Wood, 2 Iron)")
        print("10. Wooden Torch (2 Wood)")
        print("11. Diamond Armor (10 Diamond)")
        
        c_choice = input("What do you want to craft? ")
        
        if c_choice == "1":
            if wood >= 5:
                wood = wood - 5
                pickaxe_level = 1
                xp = xp + 10
                print("Crafted Wooden Pickaxe!")
                action_taken = True
            else:
                print("Not Enough Resources!")
        elif c_choice == "2":
            if wood >= 3 and stone >= 5:
                wood = wood - 3
                stone = stone - 5
                pickaxe_level = 2
                xp = xp + 20
                print("Crafted Stone Pickaxe!")
                action_taken = True
            else:
                print("Not Enough Resources!")
        elif c_choice == "3":
            if wood >= 3 and iron >= 5:
                wood = wood - 3
                iron = iron - 5
                pickaxe_level = 3
                xp = xp + 30
                print("Crafted Iron Pickaxe!")
                action_taken = True
            else:
                print("Not Enough Resources!")
        elif c_choice == "4":
            if wood >= 3 and diamond >= 5:
                wood = wood - 3
                diamond = diamond - 5
                pickaxe_level = 4
                xp = xp + 50
                print("Crafted Diamond Pickaxe!")
                action_taken = True
            else:
                print("Not Enough Resources!")
        elif c_choice == "5":
            if wood >= 3:
                wood = wood - 3
                sword_level = 1
                xp = xp + 10
                print("Crafted Wooden Sword!")
                action_taken = True
            else:
                print("Not Enough Resources!")
        elif c_choice == "6":
            if wood >= 1 and stone >= 3:
                wood = wood - 1
                stone = stone - 3
                sword_level = 2
                xp = xp + 20
                print("Crafted Stone Sword!")
                action_taken = True
            else:
                print("Not Enough Resources!")
        elif c_choice == "7":
            if wood >= 1 and iron >= 3:
                wood = wood - 1
                iron = iron - 3
                sword_level = 3
                xp = xp + 30
                print("Crafted Iron Sword!")
                action_taken = True
            else:
                print("Not Enough Resources!")
        elif c_choice == "8":
            if wood >= 1 and diamond >= 3:
                wood = wood - 1
                diamond = diamond - 3
                sword_level = 4
                xp = xp + 50
                print("Crafted Diamond Sword!")
                action_taken = True
            else:
                print("Not Enough Resources!")
        elif c_choice == "9":
            if wood >= 5 and iron >= 2:
                wood = wood - 5
                iron = iron - 2
                shield = 1
                xp = xp + 20
                print("Crafted Shield!")
                action_taken = True
            else:
                print("Not Enough Resources!")
        elif c_choice == "10":
            if wood >= 2:
                wood = wood - 2
                torch = 1
                xp = xp + 5
                print("Crafted Wooden Torch!")
                action_taken = True
            else:
                print("Not Enough Resources!")
        elif c_choice == "11":
            if diamond >= 10:
                diamond = diamond - 10
                armor = 1
                xp = xp + 100
                print("Crafted Diamond Armor!")
                action_taken = True
            else:
                print("Not Enough Resources!")
        else:
            print("Invalid choice.")
            
    elif choice == "3":
        print("\n--- Fight ---")
        print("1. Zombie (Easy)")
        print("2. Skeleton (Normal)")
        print("3. Creeper (Hard)")
        print("4. Enderman (Very Hard)")
        print("5. Dragon (Final Boss)")
        
        f_choice = input("Who do you want to fight? ")
        
        if f_choice == "1":
            if sword_level >= 1:
                print("You defeated the Zombie!")
                xp = xp + 20
                enemies_defeated = enemies_defeated + 1
            else:
                print("Without a sword, the Zombie hurt you!")
                health = health - 20
            action_taken = True
        elif f_choice == "2":
            if sword_level >= 2:
                print("You defeated the Skeleton!")
                xp = xp + 30
                enemies_defeated = enemies_defeated + 1
            else:
                print("The Skeleton shot you! You need a better sword.")
                health = health - 30
            action_taken = True
        elif f_choice == "3":
            if sword_level >= 3:
                print("You defeated the Creeper before it exploded!")
                xp = xp + 40
                enemies_defeated = enemies_defeated + 1
            else:
                print("The Creeper exploded!")
                health = health - 50
            action_taken = True
        elif f_choice == "4":
            if sword_level >= 3: # Iron Sword required
                print("You defeated the Enderman!")
                xp = xp + 50
                enemies_defeated = enemies_defeated + 1
            else:
                print("The Enderman is too strong! You need an Iron Sword.")
                health = health - 60
            action_taken = True
        elif f_choice == "5":
            if sword_level == 4 and health > 70:
                print("You valiantly fought and defeated the Ender Dragon!")
                xp = xp + 1000
                enemies_defeated = enemies_defeated + 1
                ach_dragon_slayer = 1
                print("Achievement Unlocked: 🐉 Dragon Slayer")
                
                print("\n*** YOU HAVE COMPLETED THE FINAL MISSION! ***")
                win = True
            else:
                print("You are not prepared! You need a Diamond Sword and Health > 70.")
                health = health - 80
            action_taken = True
        else:
            print("Invalid choice.")
            
    elif choice == "4":
        print("\n--- Building ---")
        print("1. Build Wood House (20 Wood, 10 Stone)")
        print("2. Upgrade to Stone House (30 Stone)")
        print("3. Upgrade to Iron House (30 Iron)")
        print("4. Upgrade to Castle (50 Stone, 20 Diamond)")
        print("5. Build Farm (10 Wood, 10 Stone)")
        print("6. Build Furnace (10 Stone)")
        
        b_choice = input("What do you want to build? ")
        
        if b_choice == "1":
            if house_level == 0 and wood >= 20 and stone >= 10:
                wood = wood - 20
                stone = stone - 10
                house_level = 1
                xp = xp + 30
                print("Built a Wood House!")
                action_taken = True
            else:
                print("Cannot build! Need 20 Wood, 10 Stone, and no existing house.")
        elif b_choice == "2":
            if house_level == 1 and stone >= 30:
                stone = stone - 30
                house_level = 2
                xp = xp + 50
                print("Upgraded to Stone House!")
                action_taken = True
            else:
                print("Need Wood House and 30 Stone.")
        elif b_choice == "3":
            if house_level == 2 and iron >= 30:
                iron = iron - 30
                house_level = 3
                xp = xp + 80
                print("Upgraded to Iron House!")
                action_taken = True
            else:
                print("Need Stone House and 30 Iron.")
        elif b_choice == "4":
            if house_level == 3 and stone >= 50 and diamond >= 20:
                stone = stone - 50
                diamond = diamond - 20
                house_level = 4
                xp = xp + 200
                print("Built a Castle!")
                action_taken = True
            else:
                print("Need Iron House, 50 Stone, and 20 Diamond.")
        elif b_choice == "5":
            if farm == 0 and wood >= 10 and stone >= 10:
                wood = wood - 10
                stone = stone - 10
                farm = 1
                xp = xp + 30
                print("Built a Farm!")
                action_taken = True
            else:
                print("Need 10 Wood and 10 Stone.")
        elif b_choice == "6":
            if furnace == 0 and stone >= 10:
                stone = stone - 10
                furnace = 1
                xp = xp + 20
                print("Built a Furnace!")
                action_taken = True
            else:
                print("Need 10 Stone.")
        else:
            print("Invalid choice.")
            
    elif choice == "5":
        print("\n======== PLAYER REPORT ========")
        print("Health:", health)
        print("Hunger:", hunger)
        print("XP:", xp)
        print("Level:", level)
        print("Wood:", wood)
        print("Stone:", stone)
        print("Coal:", coal)
        print("Iron:", iron)
        print("Gold:", gold)
        print("Diamond:", diamond)
        print("Food:", food)
        print("Sword Level:", sword_level)
        print("Shield Built:", shield)
        print("Pickaxe Level:", pickaxe_level)
        print("Armor Built:", armor)
        print("House Level:", house_level)
        print("Farm Built:", farm)
        print("Furnace Built:", furnace)
        print("Enemies Defeated:", enemies_defeated)
        print("Current Day:", day)
        print("===============================\n")
        
    elif choice == "6":
        if food > 0:
            food = food - 1
            hunger = hunger + 20
            if hunger > 100:
                hunger = 100
            print("You ate some food. Hunger is now", hunger)
            action_taken = True
        else:
            print("You don't have any food!")
            
    elif choice == "7":
        print("You sleep for the night.")
        
        if  health <100:
            health = 100
        day = day + 1
        action_taken = True
        
        # Farm production
        if farm == 1:
            food = food + 2
            print("Your farm produced 2 Food overnight!")
            
        # Random Events
        if day % 5 == 0:
            print("WARNING! Monster Attack during the night!")
            if sword_level > 0:
                print("You defended yourself with your sword!")
                xp = xp + 20
            else:
                print("You had no sword! You took 20 damage.")
                health = health - 20
        elif day % 7 == 0:
            print("It rained! Crops grew faster.")
            if farm == 1:
                food = food + 3
                print("Farm produced 3 extra Food.")
        elif day % 13 == 0:
            print("EARTHQUAKE! Your house took damage.")
            if house_level > 0:
                house_level = house_level - 1
                print("Your house level decreased.")
        elif day % 10 == 0:
            print("You found a Treasure Chest! +50 XP.")
            xp = xp + 50
            
    elif choice == "8":
        print("Exiting game...")
        game_over = True
        
    else:
        print("Invalid choice.")
        
    # --- Post-Action Checks ---
    if action_taken:
        hunger = hunger - 1
        if hunger <= 0:
            hunger = 0
            health = health - 5
            print("You are starving! Health -5")
            
        # Level Up
        if level == 1 and xp >= 100:
            level = 2
            print("LEVEL UP! You are now Level 2.")
        elif level == 2 and xp >= 250:
            level = 3
            print("LEVEL UP! You are now Level 3.")
        elif level == 3 and xp >= 500:
            level = 4
            print("LEVEL UP! You are now Level 4.")
        elif level == 4 and xp >= 800:
            level = 5
            print("LEVEL UP! You are now Level 5.")
        elif level == 5 and xp >= 1200:
            level = 6
            print("LEVEL UP! You are now Level 6.")
        elif level == 6 and xp >= 1700:
            level = 7
            print("LEVEL UP! You are now Level 7.")
        elif level == 7 and xp >= 2300:
            level = 8
            print("LEVEL UP! You are now Level 8.")
        elif level == 8 and xp >= 3000:
            level = 9
            print("LEVEL UP! You are now Level 9.")
        elif level == 9 and xp >= 4000:
            level = 10
            print("LEVEL UP! You are now Level 10.")
            
        # Achievements Check
        if ach_first_tree == 0 and wood > 0:
            ach_first_tree = 1
            print("Achievement Unlocked: 🌳 First Tree")
            
        if ach_first_pickaxe == 0 and pickaxe_level > 0:
            ach_first_pickaxe = 1
            print("Achievement Unlocked: ⛏ First Pickaxe")
            
        if ach_diamond_hunter == 0 and diamond > 0:
            ach_diamond_hunter = 1
            print("Achievement Unlocked: 💎 Diamond Hunter")
            
        if ach_home_builder == 0 and house_level > 0:
            ach_home_builder = 1
            print("Achievement Unlocked: 🏠 Home Builder")
            
        if ach_warrior == 0 and sword_level > 0:
            ach_warrior = 1
            print("Achievement Unlocked: 🛡 Warrior")
            
        if ach_king == 0 and house_level == 4:
            ach_king = 1
            print("Achievement Unlocked: 👑 King")
            
        if ach_farmer == 0 and farm == 1:
            ach_farmer = 1
            print("Achievement Unlocked: 🌾 Farmer")
            
        if ach_monster_hunter == 0 and enemies_defeated >= 100:
            ach_monster_hunter = 1
            print("Achievement Unlocked: ⚔ Monster Hunter")

if win:
    print("\n==========================================")
    print("CONGRATULATIONS! YOU BEAT MINECRAFT CLI!")
    print("==========================================")
