Places = [
    {
        "location": 'Century',
        "reasons": "For school and sports",
        "address": "2000 SE Century Blvd, Hillsboro, OR 97123"
    },
    {
        "location": 'home1',
        "reasons": "sleeping and hanging out with my mom",
        "address": "5667 SE Pine St",
        "time_to": {"Century": "3 min"}
    },
    {
        "location": 'home2',
        "reasons": "my dad's house where I live",
        "address": "7767 SW Ave",
        "time_to": {"Century": "15 - 20 min"}
    }
]

def main():
    print("Available Places:")
    for place in Places:
        print(f"{place['location']} - {place['reasons']}")

    userInputOuterKey = input("Enter the place you want to see: ")

    # Check if the user input is a valid place
    place_found = False
    for place in Places:
        if place["location"] == userInputOuterKey:
            place_found = True
            userInputInnerKey = input(f"Enter the information you want to see for {userInputOuterKey} (location, reasons, address, or time_to): ")
            if userInputInnerKey in place:
                print(f"{userInputInnerKey}: {place[userInputInnerKey]}")
            else:
                print(f"{userInputInnerKey} not found for {userInputOuterKey}")
            break

    if not place_found:
        print(f"Place '{userInputOuterKey}' not found.")

def add_location():
    check = input("do you want to add a location? (Yes : No) ")
    if check == "Yes":
        new_location = input("Name your location: ")
        Places.append(new_location)
        Places[3]["location"] = new_location

        user_ask = input("what would you like to add in this location? \n 1: reasons \n 2:address \n 3: time_too \n 4: All of them ")
        
        if user_ask == 1:
            user_add_reason
            Places[3]["reasons"] = user_add_reason

        elif user_ask == 2:
            user_add_address
            Places[3]["address"] = user_add_address

        elif user_ask == 3:
            user_add_time
            Places[3]["time_to"] = user_add_time

        elif user_ask == 4:
            user_add_reason
            Places[3]["reasons"] = user_add_reason

            user_add_address
            Places[3]["address"] = user_add_address

            user_add_time
            Places[3]["time_to"] = user_add_time

    elif check == "No":
        main()
    user_add_reason=(f"you chose to add a reason to '{new_location}'")
    user_add_address=(f"you chose to add a address to '{new_location}' what is the address?: ")
    user_add_time = (f"you chose to add time too'{new_location}'how far is it?")






add_location()