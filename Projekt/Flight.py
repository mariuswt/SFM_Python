from datetime import datetime
import random
from Projekt.StartLandingData import StartLandingData


class Flight:
    status = ("Flying", "Landing", "Parking", "Starting")
    default_time = "01.01.69 00:00:00"

    def __init__(self, airline: str, aircraft_type: str):
        self.__airline = airline
        self.__aircraft_type = aircraft_type
        self.__aircraft_status = Flight.status[0]
        self.__flight_number: str = airline[0:2].upper() + str(random.randint(100, 999))
        self.__parking_spot: int = 0
        self.landing_data: StartLandingData = StartLandingData(Flight.default_time, Flight.default_time, 0)
        self.starting_data: StartLandingData = StartLandingData(Flight.default_time, Flight.default_time, 0)

    def show_flight_data(self):
        print(f"Airline:    {self.__airline}\n"
              f"Aircraft:   {self.__aircraft_type}\n"
              f"FlightNr:   {self.__flight_number}\n"
              f"Status:     {self.__aircraft_status}\n"
              f"ParkingSpot:    {self.__parking_spot}\n"
              f"Landing:  Scheduled: {self.landing_data.scheduled_time} -  Actual: {self.landing_data.actual_time} "
              f"- Strip: {self.landing_data.strip_number}\n"
              f"Starting: Scheduled: {self.starting_data.scheduled_time} -  Actual: {self.starting_data.actual_time} "
              f"- Strip: {self.starting_data.strip_number}\n"
              )

    def edit_flight(self):
        if self.__aircraft_status == "Flying":
            while self.landing_data.scheduled_time == datetime.strptime(Flight.default_time, self.landing_data.format_data):
                date_time = input("Schedule Landing Date Time >> DD.MM.YY HH:MM:SS <<")
                try:
                    self.landing_data.scheduled_time = date_time
                    print(f"Landing:  Scheduled: {self.landing_data.scheduled_time} -  "
                          f"Actual: {self.landing_data.actual_time}\n")
                except:
                    print("WRONG FORMAT!\n")

            choice = input("Land the Flight? YES/NO").lower()
            if choice == "yes":
                self.__land_airplane()

    def __land_airplane(self):
        while self.landing_data.strip_number == 0:
            choice = input("Choose Landing Strip: 1 - 10")

        pass

fl = Flight("Airbus", "gutav200")
fl.show_flight_data()
fl.edit_flight()
fl.show_flight_data()
print(datetime.now().date())
