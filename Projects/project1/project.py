trip_name = ""
traveler_name = ""
start_location = ""
destination = ""
numberOfdays = 0
travelers = 0
purpose = ""
travel_mode = ""
trip_status = "Planned"
night = 0
airlines = ""
flight_no = ""
departure = ""
arrival = ""
ticket_price = 0
seat_preference = ""
baggage = ""
baggage_price = 0
payment_method = ""
payment_status = ""
booking_status = ""
total_price = 0

# Train Booking Variables
train_name = ""
train_no = ""
coach_type = ""
berth_preference = ""
seat_no = ""
pnr_no = ""
boarding_station = ""
drop_station = ""
departure_time = ""
arrival_time = ""
journey_date = ""
train_ticket_price = 0

# Bus Booking Variables
bus_name = ""
bus_no = ""
bus_type = ""
boarding_point = ""
dropping_point = ""
boarding_time = ""
seat_type = ""
bus_ticket_price = 0

car_name = ""
car_type = ""
car_number = ""
fuel_type = ""
driver_required = ""
pickup_location = ""
drop_location = ""
pickup_date = ""
pickup_time = ""
return_date = ""
return_time = ""
rent_per_day = 0
security_deposit = 0

bike_name = ""
bike_number = ""
bike_type = ""
helmet = ""

# Hotel Booking Variables

hotel = ""
hotel_type = ""
room_type = ""
room_number = ""
check_in_date = ""
check_out_date = ""
meal_plan = ""
bed_type = ""
hotel_address = ""

rooms = 0

room_price = 0
meal_price = 0
hotel_total = 0

hotel_payment_method = ""
hotel_payment_status = ""
hotel_booking_status = ""
id_card = ""
ticket = ""
hotel_doc = ""
while True:
    print("=" * 32)
    print("   ✈️ Travel Itinerary Planner")
    print("=" * 32)

    print("\n1. Create Trip")
    print("2. Travel Booking")
    print("3. Hotel Booking")
    print("4. Trip Cost")
    print("5. Budget")
    print("6. Documents")
    print("7. Packing List")
    print("8. Travel Report")
    print("9. Exit")

    choice = int(input("\nEnter Your Choice : "))

    match choice:

        case 1:
            print("=" * 40)
            print("            CREATE A TRIP")
            print("=" * 40)

            trip_name = input("Enter Trip Name            : ").lower()
            traveler_name = input("Enter Traveler Name        : ").lower()
            start_location = input("Enter Starting Location    : ").lower()
            destination = input("Enter Destination          : ").lower()
            numberOfdays = int(input("Enter Number of Days       : "))

            # night caculation
            if numberOfdays > 0:
                night = numberOfdays - 1
            else:
                night = 0

            travelers = int(input("Enter Number of Travelers  : "))

            while True:
                print("\nSelect Purpose of Trip")
                print("1. Vacation")
                print("2. Business")
                print("3. Family")
                print("4. Education")
                print("5. Adventure")
                print("6. Other")

                choice = input("Enter your choice (1-6): ")

                if choice == "1":
                    purpose = "Vacation"
                    break
                elif choice == "2":
                    purpose = "Business"
                    break
                elif choice == "3":
                    purpose = "Family"
                    break
                elif choice == "4":
                    purpose = "Education"
                    break
                elif choice == "5":
                    purpose = "Adventure"
                    break
                elif choice == "6":
                    purpose = input("Enter Your Purpose: ")
                    break
                else:
                    print("Invalid choice! Please try again.")

            while True:
                print("\nSelect Travel Mode")
                print("1. Flight")
                print("2. Train")
                print("3. Bus")
                print("4. Car")
                print("5. Bike")

                choice = input("Enter your choice (1-7): ")

                match choice:
                    case "1":
                        travel_mode = "Flight"
                        break
                    case "2":
                        travel_mode = "Train"
                        break
                    case "3":
                        travel_mode = "Bus"
                        break
                    case "4":
                        travel_mode = "Car"
                        break
                    case "5":
                        travel_mode = "Bike"
                        break

                    case _:
                        print(
                            "Invalid choice! Please enter a number between 1 and 5."
                        )

            print("\nTrip Created Successfully!")

            print("=" * 40)
            print("           TRIP SUMMARY")
            print("=" * 40)
            print("Trip Name           :", trip_name.capitalize())
            print("Traveler Name       :", traveler_name.capitalize())
            print("Starting Location   :", start_location.capitalize())
            print("Destination         :", destination.capitalize())
            print(f"Duration            : {numberOfdays} Days/ {night} Nights")

            print("Number of Travelers :", travelers)
            print("Purpose             :", purpose.capitalize())
            print("Travel Mode         :", travel_mode.capitalize())
            print("=" * 40)

        case 2 | 3 | 4 | 5 | 6 | 7 | 8 if trip_name == "":
            print("\n[!] Please create a trip first (Option 1)!\n")

        case 2:
            print("\n------ Travel BOOKING ------")
            print(travel_mode)

            if travel_mode.lower() == "flight":
                print("=" * 40)
                print("           Flight Booking")
                print("=" * 40)
                print(f"From             : {start_location} ")
                print(f"To               : {destination}")
                print(f"Passengers       : {travelers}")

                # select airlines

                while True:
                    print("\nSelect Airlines")
                    print("1. Indigo")
                    print("2. Air India")

                    choice = input("Enter your choice (1-2): ")

                    match choice:
                        case "1":
                            airlines = "Indigo"
                            print("\nAvailable Flights")
                            print("1. ID-01 | 07:20 AM - 09:10 AM | ₹4200")
                            print("2. ID-02 | 02:30 PM - 04:20 PM | ₹4700")

                            flight_choice = input("Select Flight : ")

                            match flight_choice:
                                case "1":
                                    flight_no = "ID-01"
                                    departure = "07:20 AM"
                                    arrival = "09:10 AM"
                                    ticket_price = 4200
                                case "2":
                                    flight_no = "ID-02"
                                    departure = "02:30 PM"
                                    arrival = "04:20 PM"
                                    ticket_price = 4700
                                case _:
                                    print("Invalid Flight")
                            break
                        case "2":
                            airlines = "Air India"
                            print("\nAvailable Flights")
                            print("1. AI-01 | 09:15 AM - 11:30 AM | ₹5100")
                            print("2. AI-02 | 06:45 PM - 08:55 PM | ₹5600")

                            flight_choice = input("Select Flight : ")

                            match flight_choice:
                                case "1":
                                    flight_no = "AI-01"
                                    departure = "09:15 AM"
                                    arrival = "11:30 AM"
                                    ticket_price = 5100
                                case "2":
                                    flight_no = "AI-02"
                                    departure = "06:45 PM"
                                    arrival = "08:55 PM"
                                    ticket_price = 5600
                                case _:
                                    print("Invalid Flight")

                            break

                        case _:
                            print(
                                "Invalid choice! Please enter a number between 1 and 4."
                            )

                while True:
                    seat_choice = input(
                        "\nSelect Seat Preference\n1. Window\n2. Aisle\n3. Middle\nEnter Choice : "
                    )
                    if seat_choice == "1":
                        seat_preference = "Window"
                        break
                    elif seat_choice == "2":
                        seat_preference = "Aisle"
                        break
                    elif seat_choice == "3":
                        seat_preference = "Middle"
                        break
                    else:
                        print("Invalid Choice! Please Try Again.")

                while True:
                    baggage_choice = input(
                        "\nSelect Check-in Baggage\n1. 15kg-₹0\n2. 20kg-₹500\n3. 25kg-₹1000\nEnter Choice : "
                    )
                    if baggage_choice == "1":
                        baggage = "15 kg"
                        baggage_price = 0
                        break
                    elif baggage_choice == "2":
                        baggage = "20 kg"
                        baggage_price = 500
                        break
                    elif baggage_choice == "3":
                        baggage = "25 kg"
                        baggage_price = 1000
                        break
                    else:
                        print("Invalid Choice! Please Try Again.")

                while True:
                    payment_choice = input(
                        "\nSelect Payment\n1. UPI\n2. Debit\n3. Credit\n4. NetBanking\n5. Cash\nEnter Choice : "
                    )
                    if payment_choice == "1":
                        payment_method = "UPI"
                        break
                    elif payment_choice == "2":
                        payment_method = "Debit Card"
                        break
                    elif payment_choice == "3":
                        payment_method = "Credit Card"
                        break
                    elif payment_choice == "4":
                        payment_method = "Net Banking"
                        break
                    elif payment_choice == "5":
                        payment_method = "Cash"
                        break
                    else:
                        print("Invalid Choice! Please Try Again.")

                total_price = ticket_price + baggage_price

                print("\nTotal Amount : ₹", total_price)

                confirm = input("Proceed with Payment? (yes/no) : ")

                if confirm.lower() == "yes":
                    payment_status = "Successful"
                    booking_status = "Confirmed"
                else:
                    payment_status = "Cancelled"
                    booking_status = "Pending"

                print("=" * 45)
                print("         BOOKING CONFIRMED")
                print("=" * 45)
                booking_id = "BK-" + flight_no

                print("Booking ID        :", booking_id)
                print("Passenger Name    :", traveler_name)
                print("Airline           :", airlines)
                print("Flight Number     :", flight_no)
                print("From              :", start_location)
                print("To                :", destination)
                print("Departure Time    :", departure)
                print("Arrival Time      :", arrival)
                print("Seat Preference   :", seat_preference)
                print("Check-in Baggage  :", baggage)
                print("Payment Method    :", payment_method)
                print("Payment Status    :", payment_status)
                print("Ticket Price      : ₹", ticket_price)
                print("Baggage Charge    : ₹", baggage_price)
                print("-" * 45)
                print("Total Amount      : ₹", total_price)
                print("Payment Method    : ₹", payment_method)
                print("Booking Status    :", booking_status)
                print(f"Include Travellers: {total_price*travelers}")

                print("=" * 45)

            elif travel_mode.lower() == "train":
                print("\n==============================")
                print("      TRAIN BOOKING")
                print("==============================")

                boarding_station = start_location
                drop_station = destination

                journey_date = input("Enter Journey Date (DD/MM/YYYY): ")

                while True:

                    print("\nAvailable Trains")
                    print("1. Vande Bharat Express")
                    print("2. Rajdhani Express")

                    train_choice = input("Select Train : ")

                    match train_choice:

                        case "1":
                            train_name = "Vande Bharat Express"
                            train_no = "22436"
                            departure_time = "06:00 AM"
                            arrival_time = "11:30 AM"
                            train_ticket_price = 1800
                            break

                        case "2":
                            train_name = "Rajdhani Express"
                            train_no = "12951"
                            departure_time = "08:30 PM"
                            arrival_time = "06:15 AM"
                            train_ticket_price = 2200
                            break

                        case _:
                            print("Invalid Choice")

                while True:
                    coach_choice = input(
                        "\nSelect Coach\n1. Sleeper\n2. AC 3 Tier\n3. AC 2 Tier\n4. First AC\nEnter Choice : "
                    )
                    if coach_choice == "1":
                        coach_type = "Sleeper"
                        train_ticket_price += 0
                        break
                    elif coach_choice == "2":
                        coach_type = "AC 3 Tier"
                        train_ticket_price += 500
                        break
                    elif coach_choice == "3":
                        coach_type = "AC 2 Tier"
                        train_ticket_price += 900
                        break
                    elif coach_choice == "4":
                        coach_type = "First AC"
                        train_ticket_price += 1800
                        break
                    else:
                        print("Invalid Choice")

                while True:
                    berth_choice = input(
                        "\nBerth Preference\n1. Lower\n2. Middle\n3. Upper\n4. Side Lower\n5. Side Upper\nEnter Choice : "
                    )
                    if berth_choice == "1":
                        berth_preference = "Lower"
                        break
                    elif berth_choice == "2":
                        berth_preference = "Middle"
                        break
                    elif berth_choice == "3":
                        berth_preference = "Upper"
                        break
                    elif berth_choice == "4":
                        berth_preference = "Side Lower"
                        break
                    elif berth_choice == "5":
                        berth_preference = "Side Upper"
                        break
                    else:
                        print("Invalid Choice")

                while True:
                    payment = input(
                        "\nSelect Payment Method\n1. UPI\n2. Debit Card\n3. Credit Card\n4. Cash\nEnter Choice : "
                    )
                    if payment == "1":
                        payment_method = "UPI"
                        break
                    elif payment == "2":
                        payment_method = "Debit Card"
                        break
                    elif payment == "3":
                        payment_method = "Credit Card"
                        break
                    elif payment == "4":
                        payment_method = "Cash"
                        break
                    else:
                        print("Invalid Choice")

                payment_status = "Successful"
                booking_status = "Confirmed"

                total_price = train_ticket_price * travelers

                seat_no = "B2-45"
                pnr_no = "4567891230"

                print("\n====================================")
                print("      TRAIN BOOKING SUCCESSFUL")
                print("====================================")

                print("Trip Name        :", trip_name)
                print("Passenger        :", traveler_name)
                print("Train            :", train_name)
                print("Train No         :", train_no)
                print("Boarding         :", boarding_station)
                print("Destination      :", drop_station)
                print("Journey Date     :", journey_date)
                print("Departure        :", departure_time)
                print("Arrival          :", arrival_time)
                print("Coach            :", coach_type)
                print("Berth            :", berth_preference)
                print("Seat             :", seat_no)
                print("PNR Number       :", pnr_no)
                print("Passengers       :", travelers)
                print("Ticket Price     :", train_ticket_price)
                print("Total Amount     :", total_price)
                print("Payment Method   :", payment_method)
                print("Payment Status   :", payment_status)
                print("Booking Status   :", booking_status)

            elif travel_mode.lower() == "bus":
                print("\n==========================")
                print("       BUS BOOKING")
                print("==========================")

                boarding_point = start_location
                dropping_point = destination

                journey_date = input("Enter Journey Date (DD/MM/YYYY) : ")

                while True:

                    print("\nAvailable Buses")
                    print("1. Volvo AC Sleeper")
                    print("2. Volvo AC Seater")

                    bus_choice = input("Enter Choice : ")

                    match bus_choice:

                        case "1":
                            bus_name = "Volvo AC Sleeper"
                            bus_no = "MP09VB101"
                            boarding_time = "09:00 PM"
                            arrival_time = "06:00 AM"
                            bus_ticket_price = 1200
                            break

                        case "2":
                            bus_name = "Volvo AC Seater"
                            bus_no = "MP09VB202"
                            boarding_time = "08:00 AM"
                            arrival_time = "03:00 PM"
                            bus_ticket_price = 900
                            break

                        case _:
                            print("Invalid Choice")

                while True:
                    seat_choice = input(
                        "\nSeat Preference\n1. Window\n2. Aisle\nEnter Choice : "
                    )
                    if seat_choice == "1":
                        seat_type = "Window"
                        break
                    elif seat_choice == "2":
                        seat_type = "Aisle"
                        break
                    else:
                        print("Invalid Choice")

                while True:
                    payment = input(
                        "\nSelect Payment Method\n1. UPI\n2. Debit Card\n3. Credit Card\n4. Cash\nEnter Choice : "
                    )
                    if payment == "1":
                        payment_method = "UPI"
                        break
                    elif payment == "2":
                        payment_method = "Debit Card"
                        break
                    elif payment == "3":
                        payment_method = "Credit Card"
                        break
                    elif payment == "4":
                        payment_method = "Cash"
                        break
                    else:
                        print("Invalid Choice")

                payment_status = "Successful"
                booking_status = "Confirmed"

                seat_no = "W12"

                total_price = bus_ticket_price * travelers

                print("\n===================================")
                print("      BUS BOOKING CONFIRMED")
                print("===================================")

                print("Trip Name        :", trip_name)
                print("Passenger        :", traveler_name)
                print("Bus              :", bus_name)
                print("Bus Number       :", bus_no)
                print("Boarding         :", boarding_point)
                print("Dropping         :", dropping_point)
                print("Journey Date     :", journey_date)
                print("Departure        :", boarding_time)
                print("Arrival          :", arrival_time)
                print("Seat Preference  :", seat_type)
                print("Seat Number      :", seat_no)
                print("Passengers       :", travelers)
                print("Ticket Price     :", bus_ticket_price)
                print("Total Amount     :", total_price)
                print("Payment Method   :", payment_method)
                print("Payment Status   :", payment_status)
                print("Booking Status   :", booking_status)

            elif travel_mode.lower() == "car":
                print("\n============================")
                print("CAR BOOKING".center(10))
                print("============================")

                pickup_location = start_location
                drop_location = destination

                pickup_date = input("Enter Pickup Date (DD/MM/YYYY) : ")
                pickup_time = input("Enter Pickup Time (HH:MM) : ")

                return_date = input("Enter Return Date (DD/MM/YYYY) : ")
                return_time = input("Enter Return Time (HH:MM) : ")

                while True:

                    print("\nAvailable Cars")
                    print("1. Maruti Swift")
                    print("2. Hyundai Creta")

                    car_choice = input("Enter Choice : ")

                    match car_choice:

                        case "1":
                            car_name = "Maruti Swift"
                            car_number = "MP09AB1234"
                            fuel_type = "Petrol"
                            rent_per_day = 1500
                            break

                        case "2":
                            car_name = "Hyundai Creta"
                            car_number = "MP09CD5678"
                            fuel_type = "Diesel"
                            rent_per_day = 2500
                            break

                        case _:
                            print("Invalid Choice")

                while True:
                    type_choice = input(
                        "\nCar Type\n1. Self Drive\n2. With Driver\nEnter Choice : "
                    )
                    if type_choice == "1":
                        car_type = "Self Drive"
                        driver_required = "No"
                        break
                    elif type_choice == "2":
                        car_type = "With Driver"
                        driver_required = "Yes"
                        rent_per_day += 500
                        break
                    else:
                        print("Invalid Choice")

                while True:
                    payment = input(
                        "\nSelect Payment Method\n1. UPI\n2. Debit Card\n3. Credit Card\n4. Cash\nEnter Choice : "
                    )
                    if payment == "1":
                        payment_method = "UPI"
                        break
                    elif payment == "2":
                        payment_method = "Debit Card"
                        break
                    elif payment == "3":
                        payment_method = "Credit Card"
                        break
                    elif payment == "4":
                        payment_method = "Cash"
                        break
                    else:
                        print("Invalid Choice")

                security_deposit = 3000

                total_price = (rent_per_day * numberOfdays) + security_deposit

                payment_status = "Successful"
                booking_status = "Confirmed"

                print("\n===================================")
                print("      CAR BOOKING CONFIRMED")
                print("===================================")

                print("Trip Name          :", trip_name)
                print("Traveler           :", traveler_name)
                print("Car                :", car_name)
                print("Vehicle Number     :", car_number)
                print("Fuel Type          :", fuel_type)
                print("Booking Type       :", car_type)
                print("Driver Required    :", driver_required)
                print("Pickup             :", pickup_location)
                print("Drop               :", drop_location)
                print("Pickup Date        :", pickup_date)
                print("Pickup Time        :", pickup_time)
                print("Return Date        :", return_date)
                print("Return Time        :", return_time)
                print("Days               :", numberOfdays)
                print("Rent Per Day       :", rent_per_day)
                print("Security Deposit   :", security_deposit)
                print("Total Amount       :", total_price)
                print("Payment Method     :", payment_method)
                print("Payment Status     :", payment_status)
                print("Booking Status     :", booking_status)

            else:
                print("\n===========================")
                print("      BIKE BOOKING")
                print("===========================")

                pickup_location = start_location
                drop_location = destination

                pickup_date = input("Enter Pickup Date (DD/MM/YYYY) : ")
                pickup_time = input("Enter Pickup Time (HH:MM) : ")

                return_date = input("Enter Return Date (DD/MM/YYYY) : ")
                return_time = input("Enter Return Time (HH:MM) : ")

                while True:

                    print("\nAvailable Bikes")
                    print("1. Hero Splendor")
                    print("2. Honda Shine")

                    bike_choice = input("Enter Choice : ")

                    match bike_choice:

                        case "1":
                            bike_name = "Hero Splendor"
                            bike_number = "MP09BK101"
                            bike_type = "Commuter"
                            rent_per_day = 500
                            break

                        case "2":
                            bike_name = "Honda Shine"
                            bike_number = "MP09BK202"
                            bike_type = "Commuter"
                            rent_per_day = 600
                            break

                        case _:
                            print("Invalid Choice")

                while True:
                    helmet_choice = input(
                        "\nHelmet Required?\n1. Yes\n2. No\nEnter Choice : ")
                    if helmet_choice == "1":
                        helmet = "Yes"
                        break
                    elif helmet_choice == "2":
                        helmet = "No"
                        break
                    else:
                        print("Invalid Choice")

                while True:
                    payment = input(
                        "\nSelect Payment Method\n1. UPI\n2. Debit Card\n3. Credit Card\n4. Cash\nEnter Choice : "
                    )
                    if payment == "1":
                        payment_method = "UPI"
                        break
                    elif payment == "2":
                        payment_method = "Debit Card"
                        break
                    elif payment == "3":
                        payment_method = "Credit Card"
                        break
                    elif payment == "4":
                        payment_method = "Cash"
                        break
                    else:
                        print("Invalid Choice")

                security_deposit = 1000

                total_price = (rent_per_day * numberOfdays) + security_deposit

                payment_status = "Successful"
                booking_status = "Confirmed"

                print("\n===================================")
                print("      BIKE BOOKING CONFIRMED")
                print("===================================")

                print("Trip Name          :", trip_name)
                print("Traveler           :", traveler_name)
                print("Bike               :", bike_name)
                print("Bike Number        :", bike_number)
                print("Bike Type          :", bike_type)
                print("Pickup             :", pickup_location)
                print("Drop               :", drop_location)
                print("Pickup Date        :", pickup_date)
                print("Pickup Time        :", pickup_time)
                print("Return Date        :", return_date)
                print("Return Time        :", return_time)
                print("Days               :", numberOfdays)
                print("Helmet             :", helmet)
                print("Rent Per Day       :", rent_per_day)
                print("Security Deposit   :", security_deposit)
                print("Total Amount       :", total_price)
                print("Payment Method     :", payment_method)
                print("Payment Status     :", payment_status)
                print("Booking Status     :", booking_status)

        case 3:

            print("\n==============================")
            print("HOTEL BOOKING".center(30))
            print("==============================")

            while True:

                print("\nAvailable Hotels")
                print("1. Taj Hotel")
                print("2. Radisson Blu")

                hotel_choice = input("Enter Choice : ")

                match hotel_choice:

                    case "1":
                        hotel = "Taj Hotel"
                        hotel_type = "5-Star"
                        break

                    case "2":
                        hotel = "Radisson Blu"
                        hotel_type = "5-Star"
                        break

                    case _:
                        print("Invalid Choice")

            while True:
                room_choice = input(
                    "\nSelect Room Type\n1. Standard\n2. Deluxe\n3. Suite\nEnter Choice : "
                )
                if room_choice == "1":
                    room_type = "Standard"
                    room_price = 2500
                    break
                elif room_choice == "2":
                    room_type = "Deluxe"
                    room_price = 4000
                    break
                elif room_choice == "3":
                    room_type = "Suite"
                    room_price = 7000
                    break
                else:
                    print("Invalid Choice")

            rooms = int(input("\nNumber of Rooms : "))
            nights = int(input("Number of Nights : "))

            while True:
                meal_choice = input(
                    "\nMeal Plan\n1. Breakfast\n2. Breakfast+Dinner\n3. No Meal\nEnter Choice : "
                )
                if meal_choice == "1":
                    meal = "Breakfast"
                    meal_price = 300
                    break
                elif meal_choice == "2":
                    meal = "Breakfast + Dinner"
                    meal_price = 700
                    break
                elif meal_choice == "3":
                    meal = "No Meal"
                    meal_price = 0
                    break
                else:
                    print("Invalid Choice")

            hotel_total = (room_price * rooms * nights) + (meal_price *
                                                           travelers * nights)

            while True:
                payment = input(
                    "\nSelect Payment Method\n1. UPI\n2. Debit Card\n3. Credit Card\n4. Cash\nEnter Choice : "
                )
                if payment == "1":
                    hotel_payment_method = "UPI"
                    break
                elif payment == "2":
                    hotel_payment_method = "Debit Card"
                    break
                elif payment == "3":
                    hotel_payment_method = "Credit Card"
                    break
                elif payment == "4":
                    hotel_payment_method = "Cash"
                    break
                else:
                    print("Invalid Choice")

            hotel_payment_status = "Successful"
            hotel_booking_status = "Confirmed"

            print("\n===================================")
            print("     HOTEL BOOKING CONFIRMED")
            print("===================================")

            print("Trip Name        :", trip_name)
            print("Hotel            :", hotel)
            print("Room Type        :", room_type)
            print("Rooms            :", rooms)
            print("Nights           :", nights)
            print("Meal Plan        :", meal)
            print("Room Price       :", room_price)
            print("Hotel Cost       :", hotel_total)
            print("Payment Method   :", hotel_payment_method)
            print("Payment Status   :", hotel_payment_status)
            print("Booking Status   :", hotel_booking_status)

        case 4:
            print("\n------ TRIP COST ------")

            travel_cost = total_price
            hotel_cost = hotel_total

            print("Travel Cost :", travel_cost)
            print("Hotel Cost  :", hotel_cost)

            food_cost = float(input("Enter Food Cost : "))

            total_trip_cost = travel_cost + hotel_cost + food_cost

            print("Total Trip Cost =", total_trip_cost)

        case 5:
            print("\n" + "=" * 40)
            print("            💰 TRIP BUDGET")
            print("=" * 40)

            budget = float(input("Enter your total budget for the trip : ₹"))
            spent = total_price + hotel_total

            print(f"\nCurrently Spent (Travel + Hotel) : ₹{spent}")
            extra_spent = float(input("Enter any other expenses so far  : ₹"))

            total_spent = spent + extra_spent
            remaining = budget - total_spent

            print("\n[ Budget Summary ]")
            print(f"Total Budget      : ₹{budget}")
            print(f"Total Spent       : ₹{total_spent}")

            if remaining < 0:
                print(
                    f"Status            : 🔴 Over Budget by ₹{abs(remaining)}!")
            elif remaining == 0:
                print(f"Status            : 🟡 Exactly on budget.")
            else:
                print(
                    f"Status            : 🟢 Under Budget (₹{remaining} left)")
            print("=" * 40)

        case 6:
            print("\n------ DOCUMENT CHECKLIST ------")

            if destination == "":
                print("Please create a trip first !")
            else:
                id_card = input(
                    "ID Card (Aadhaar/Voter ID) packed? (yes/no): ").lower()

                if travel_mode.lower() == "flight":
                    ticket = input(
                        "Flight Tickets & Boarding Pass packed? (yes/no): "
                    ).lower()
                elif travel_mode.lower() == "train":
                    ticket = input("Train Tickets packed? (yes/no): ").lower()
                elif travel_mode.lower() == "bus":
                    ticket = input("Bus Tickets packed? (yes/no): ").lower()
                elif travel_mode.lower() == "car" or travel_mode.lower(
                ) == "bike":
                    ticket = input(
                        "Driving License & RC packed? (yes/no): ").lower()
                else:
                    ticket = "yes"

                hotel_doc = input(
                    "Hotel Booking Confirmation packed? (yes/no): ").lower()

                print("\n[ Document Status Report ]")

                if id_card == "yes":
                    print("✔ ID Card: Ready")
                else:
                    print("❌ ID Card: MISSING! (Crucial for travel)")

                if ticket == "yes":
                    print("✔ Travel Documents: Ready")
                else:
                    print(
                        "❌ Travel Documents: MISSING! (You can't travel without this)"
                    )

                if hotel_doc == "yes":
                    print("✔ Hotel Confirmation: Ready")
                else:
                    print(
                        "❌ Hotel Confirmation: MISSING! (Keep it handy for check-in)"
                    )

        case 7:
            print("\n------ SMART PACKING LIST ------")

            if numberOfdays == 0:
                print("Please create a trip first!")
            else:
                print("\n[ Essentials ]")
                print("✔ Mobile & Charger")
                print("✔ Power Bank")
                print("✔ Toiletries (Toothbrush, Paste, Soap, Deodorant)")
                print("✔ Personal Medicines & First-Aid")
                print("✔ ID Cards, Wallet & Cash")

                print(f"\n[ Clothing for {numberOfdays} days ]")
                print(f"✔ {numberOfdays + 1} Shirts/Tops")
                print(f"✔ {max(1, numberOfdays // 2 + 1)} Trousers/Jeans")
                print(f"✔ {numberOfdays + 1} Pairs of Undergarments")
                print(f"✔ {numberOfdays} Pairs of Socks")
                print("✔ 1 Pair of Comfortable Walking Shoes")
                print("✔ 1 Pair of Slippers/Sandals")
                print("✔ 1 Light Jacket (Just in case)")

                if purpose.lower() == "business":
                    print("\n[ Business Specific ]")
                    print("✔ Laptop & Charger")
                    print("✔ Formal Wear (Suits/Blazers)")
                    print("✔ Business Cards & Documents")
                    print("✔ Notepad & Pen")
                elif purpose.lower() == "vacation" or purpose.lower(
                ) == "family":
                    print("\n[ Vacation Specific ]")
                    print("✔ Sunglasses & Sunscreen")
                    print("✔ Camera or Extra Storage for Photos")
                    print("✔ Swimwear (if going to a beach/pool)")
                    print("✔ Extra Casual Outfits")
                elif purpose.lower() == "adventure":
                    print("\n[ Adventure Specific ]")
                    print("✔ Trekking/Hiking Shoes")
                    print("✔ Flashlight/Headlamp")
                    print("✔ Water Bottle & Snacks")
                    print("✔ Mosquito Repellent")

                if travel_mode.lower() == "flight":
                    print("\n[ Flight Items ]")
                    print("✔ Flight Tickets & Boarding Pass")
                    print("✔ Neck Pillow & Earplugs")
                elif travel_mode.lower() == "car" or travel_mode.lower(
                ) == "bike":
                    print("\n[ Road Trip Items ]")
                    print("✔ Driving License")
                    print("✔ Vehicle Registration & Insurance")
                    print("✔ Playlist & Offline Maps")

        case 8:
            print("\n" + "=" * 50)
            print("              FINAL TRAVEL REPORT")
            print("=" * 50)

            if trip_name == "":
                print("\nNo trip details found.")
                print("Please create a trip first.")
            else:
                print(f"\nTraveler Name   : {traveler_name.title()}")
                print(f"Trip Name       : {trip_name.title()}")
                print(f"From            : {start_location.title()}")
                print(f"To              : {destination.title()}")
                print(f"Duration        : {numberOfdays} Days / {night} Nights")
                print(f"Purpose         : {purpose.title()}")
                print(f"Travelers       : {travelers}")

                print("\n" + "-" * 50)
                print("BOOKING DETAILS")
                print("-" * 50)

                print(f"Travel Mode     : {travel_mode.title()}")
                print(f"Travel Cost     : ₹{total_price}")

                if hotel != "":
                    print(f"Hotel           : {hotel.title()}")
                    print(f"Room Type       : {hotel_type}")
                    print(f"Hotel Cost      : ₹{hotel_total}")
                else:
                    print("Hotel           : Not Booked")

                total_trip_cost = total_price + hotel_total

                print("\n" + "-" * 50)
                print(f"Total Cost      : ₹{total_trip_cost}")
                print("-" * 50)

                print("\nDOCUMENT STATUS")

                if id_card == "yes":
                    print("ID Card         : Available")
                else:
                    print("ID Card         : Not Available")

                if ticket == "yes":
                    print("Tickets         : Available")
                else:
                    print("Tickets         : Not Available")

                if hotel != "":
                    if hotel_doc == "yes":
                        print("Hotel Receipt   : Available")
                    else:
                        print("Hotel Receipt   : Not Available")

                print("\nHave a safe journey!")

            print("=" * 50)

        case 9:
            print("\nThank You For Using Travel Itinerary Planner.")
            break

        case _:
            print("\nInvalid Choice! Please Try Again.")
