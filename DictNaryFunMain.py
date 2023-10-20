
Places = [
    {
        "location": 'Century',
        "reasons" : "For school and sports",
        "address" : "2000 SE Century Blvd, Hillsboro, OR 97123"
    },
    {
        "location": 'home1',
        "reasons" : "sleeping and hanging out with my mom", 
        "Address" : "5667 se pine st", 
        "time_to" : [{"Century": "3 min"},]
    },
    {
        "location": 'home2',
        "reasons" : "my dads house where i live",
        "Address" : "7767 sw ave",
        "time_to" : "15 - 20 min"
    },
    ]

def main():
   # Iterate through the list of places
    for place in Places:
        location = place.get("location")
        print(f"location: {location}")
    
    # Iterate through the inner dictionary
    for key_inner in Places.keys():
        print(f"Inner Key: {key_inner}")
    userInputOuterKey = str(input("what would you like to see? outerkey:"))
    userInputInnerKey = str(input("what would you like to see? innerkey:"))

    print(Places[userInputOuterKey][userInputInnerKey])
class PlaceFinder():

    def __init__(self,amntplace,):

        self.amntplace = amntplace

    def get_info_place(self,amntplace):
       for i in range(amntplace):
           eki