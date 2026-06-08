flights = {
    "AI101": {"source": "Delhi", "dest": "Mumbai", "seats": 5, "price": 5500},
    "AI102": {"source": "Mumbai", "dest": "Delhi", "seats": 8, "price": 5200}
}

source = input("Enter source: ")
dest = input("Enter destination: ")

for flight in flights:

    if flights[flight]["source"] == source and flights[flight]["dest"] == dest:

        print("Flight No:", flight)
        print("Seats:", flights[flight]["seats"])

        book = int(input("Enter seats to book: "))

        if book <= flights[flight]["seats"]:

            flights[flight]["seats"] -= book

            print("Booking Confirmed")
            print("Remaining Seats:", flights[flight]["seats"])

        else:
            print("Seats not available")
