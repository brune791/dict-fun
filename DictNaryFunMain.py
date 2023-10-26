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

if __name__ == "__main__":
    main()