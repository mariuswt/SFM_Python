import time

from Projekt.Flight import Flight
from datetime import datetime


class Airport:
    def __init__(self):
        self.landing_starting_strips = {1: "Free", 2: "Free", 3: "Free", 4: "Free"}
        self.parking_spots = {1: "Free", 2: "Free", 3: "Free", 4: "Free", 5: "Free",
                              6: "Free", 7: "Free", 8: "Free", 9: "Free", 10: "Free"}
        self.airlines: list[str] = []
        self.aircraft_types: list[str] = []
        self.flights: list[Flight] = []

    def register_new_flight(self):
        airline, aircraft_type = "", ""
        while airline == "":
            count = 0
            if len(self.airlines) != 0:
                print("Select Airline from List or input new Airline")

                for airline in self.airlines:
                    print(f"{count}: {airline}")
                    count += 1

            airline = str(input("Airline: "))
            try:
                if int(airline) in range(0, count):
                    airline = self.airlines[int(airline)]
                    print(f"selected -{airline}-\n")
            except:
                pass

        while aircraft_type == "":
            count = 0
            if len(self.aircraft_types) != 0:
                print("Select Aircraft Type from List or input new Aircraft")

                for aircraft_type in self.aircraft_types:
                    print(f"{count}: {aircraft_type}")
                    count += 1

            aircraft_type = str(input("Aircraft Type: "))

            try:
                if int(aircraft_type) in range(0, count):
                    aircraft_type = self.aircraft_types[int(aircraft_type)]
                    print(f"selected -{aircraft_type}-\n")
            except:
                pass

        if airline not in self.airlines:
            self.airlines.append(airline)
        if aircraft_type not in self.aircraft_types:
            self.aircraft_types.append(aircraft_type)

        flight = Flight(airline, aircraft_type)

        while flight.landing_data.scheduled_time == datetime.strptime(Flight.default_time,
                                                                      flight.landing_data.format_data):
            date_time = input("Schedule Landing >> DD.MM.YY HH:MM:SS <<")
            try:
                flight.landing_data.scheduled_time = date_time
                print(f"Scheduled: {flight.landing_data.scheduled_time}")
            except:
                print("WRONG FORMAT!\n")

        self.flights.append(flight)

    def show_flights(self):
        if len(self.flights) == 0:
            print("\nNo Flights Registered!\n")
            return
        print("-" * 50)
        for flight in self.flights:
            flight.show_flight_data()
        print("-" * 50)

    def edit_flights(self):
        if len(self.flights) == 0:
            print("\nNo Flights Registered!\n")
            return
        while True:
            self.show_flights()
            print("Abort with 0")
            choice = input("Select Flight by FlightNumber:")
            if choice == "0":
                print("ACTION ABORTED!\n")
                return
            for flight in self.flights:
                if flight.flight_number == choice:
                    if flight.aircraft_status == "Flying":
                        self.__land_airplane(flight)
                        return
                    elif flight.aircraft_status == "Landing":
                        self.__park_airplane(flight)
                        return
                    elif flight.aircraft_status == "Parking":
                        self.__plan_start(flight)
                        return
                    elif flight.aircraft_status == "Planing Start":
                        self.__start_airplane(flight)
                        return
                    elif flight.aircraft_status == "Starting":
                        print("Aircraft is Flying")
                        return
            print("WRONG INPUT OF FLIGHT NUMBER!")
            time.sleep(2)

    def __land_airplane(self, flight):
        if "Free" not in self.landing_starting_strips.values():
            print("\nNo Free Landing Strip!\n")
            return

        landing_strip = 0
        while landing_strip not in self.landing_starting_strips.keys():
            print(f"Landing Strips: {self.landing_starting_strips}")
            landing_strip = int(input("Select a Free Strip:  "))
            if self.landing_starting_strips[landing_strip] == "Blocked":
                landing_strip = 0
                print("Strip is Blocked!")
                time.sleep(1)

        self.landing_starting_strips[landing_strip] = "Blocked"
        flight.land_airplane(landing_strip)
        print("Landed successfully\n")

    def __park_airplane(self, flight):
        if "Free" not in self.parking_spots.values():
            print("\nNo Free Parking Spot !\n")
            return

        parking_spot = 0
        while parking_spot not in self.parking_spots.keys():
            print(f"Parking Spots: {self.parking_spots}")
            parking_spot = int(input("Select a Free Spot:  "))
            if self.parking_spots[parking_spot] == "Blocked":
                parking_spot = 0
                print("Spot is Blocked!")
                time.sleep(1)
        self.parking_spots[parking_spot] = "Blocked"
        flight.park_airplane(parking_spot)
        self.landing_starting_strips[flight.landing_data.strip_number] = "Free"
        print("Parked successfully\n")

    def __plan_start(self, flight):
        if "Free" not in self.landing_starting_strips.values():
            print("\nNo Free Starting Strip!\n")
            return

        while flight.starting_data.scheduled_time == datetime.strptime(Flight.default_time,
                                                                       flight.landing_data.format_data):
            date_time = input("Schedule Starting >> DD.MM.YY HH:MM:SS <<")
            try:
                flight.starting_data.scheduled_time = date_time
                print(f"Scheduled: {flight.starting_data.scheduled_time}")
            except:
                print("WRONG FORMAT!\n")

        starting_strip = 0
        while starting_strip not in self.landing_starting_strips.keys():
            print(f"Starting Strips: {self.landing_starting_strips}")
            starting_strip = int(input("Select a Free Strip:  "))
            if self.landing_starting_strips[starting_strip] == "Blocked":
                starting_strip = 0
                print("Strip is Blocked!")
                time.sleep(1)
        self.landing_starting_strips[starting_strip] = "Blocked"
        flight.plan_start(starting_strip)
        print("Planned successfully\n")

    def __start_airplane(self, flight):
        flight.start_airplane()
        print(f"STRIP NUMBER ")
        print(f"Started successfully on StripNumber: {flight.starting_data.strip_number}\n")
        self.parking_spots[flight.parking_spot] = "Free"
        self.landing_starting_strips[flight.starting_data.strip_number] = "Free"

    def remove_flight(self):
        if len(self.flights) == 0:
            print("No Flights Registered!")
            return
        while True:
            self.show_flights()
            choice = input("\nREMOVE Flight\nSelect Flight by Flight Number: ")
            if choice == "0":
                print("ACTION ABORTED!\n")
                return
            for flight in self.flights:
                if flight.flight_number == choice:
                    selection = input("approve removal yes/no : ").lower()
                    if selection == "yes":
                        self.flights.remove(flight)
                        print("Flight removed!")
                        return
                    if selection == "no":
                        print("Action aborted!")
                        return
            print("*" * 5, "Incorrect Flight Number", "*" * 5)
