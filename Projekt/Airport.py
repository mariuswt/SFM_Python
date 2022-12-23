import time

from Projekt.Flight import Flight
from datetime import datetime


class Airport:
    def __init__(self):
        self.landing_strips = {1: "Free", 2: "Free", 3: "Free", 4: "Free"}
        self.parking_spots = {1: "Free", 2: "Free", 3: "Free", 4: "Free", 5: "Free",
                              6: "Free", 7: "Free", 8: "Free", 9: "Free", 10: "Free"}
        self.airlines: list[str] = [""]
        self.aircraft_types: list[str] = [""]
        self.flights: list[Flight] = []

    def register_new_flight(self):
        airline, aircraft_type = "", ""
        while airline == "":
            airline = str(input("Airline: "))
        while aircraft_type == "":
            aircraft_type = input("Aircraft Type: ")

        if airline not in self.airlines:
            self.airlines += airline
        if aircraft_type not in self.aircraft_types:
            self.aircraft_types += aircraft_type

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
        for flight in self.flights:
            flight.show_flight_data()

    def edit_flights(self):
        while True:
            self.show_flights()
            choice = input("Select Flight by FlightNumber:")
            for flight in self.flights:
                if flight.flight_number == choice:
                    if flight.aircraft_status == "Flying":
                        self.land_airplane(flight)
                        return
                    elif flight.aircraft_status == "Landing":
                        return
                    elif flight.aircraft_status == "Parking":
                        return
                    elif flight.aircraft_status == "Starting":
                        return
            print("FALSCHE EINGABE DER FLUGNUMMER!")
            time.sleep(2)

    def land_airplane(self, flight):
        print(self.landing_strips)
        print("hello")

    def park_airplane(self):
        pass

    def plan_start(self):
        pass

    def start_airplane(self):
        pass

    def remove_flight(self):
        pass


a = Airport()
a.register_new_flight()
#a.show_flights()
a.edit_flights()
