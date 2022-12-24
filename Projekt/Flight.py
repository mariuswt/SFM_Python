from datetime import datetime
import random
from Projekt.StartLandingData import StartLandingData


class Flight:
    status = ("Flying", "Landing", "Parking", "Planing Start", "Started")
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

        if self.__aircraft_status == "Flying":
            print(f"\n{self.__flight_number} {self.__aircraft_status} {self.__airline} {self.__aircraft_type}\n"
                  f"Landing:  Scheduled: {self.landing_data.scheduled_time}\n")

        if self.__aircraft_status == "Landing":
            print(f"\n{self.__flight_number} {self.__aircraft_status} on Strip: {self.landing_data.strip_number}  "
                  f"{self.__airline} {self.__aircraft_type}\n"
                  f"Scheduled: {self.landing_data.scheduled_time} - Actual: {self.landing_data.actual_time} \n")

        if self.__aircraft_status == "Parking":
            print(f"\n{self.__flight_number} {self.__aircraft_status} on ParkingSpot: {self.__parking_spot} "
                  f"{self.__airline} {self.__aircraft_type}\n")

        if self.__aircraft_status == "Planing Start":
            print(f"\n{self.__flight_number} {self.__aircraft_status} on Strip: {self.starting_data.strip_number} "
                  f"{self.__airline} {self.__aircraft_type}\n"
                  f"Starting:  Scheduled: {self.starting_data.scheduled_time}\n")

        if self.__aircraft_status == "Started":
            print(f"\n{self.__flight_number} {self.__aircraft_status} on Strip: {self.starting_data.strip_number} "
                  f"{self.__airline} {self.__aircraft_type}\n"
                  f"Scheduled: {self.starting_data.scheduled_time} - Actual: {self.starting_data.actual_time}\n")

    def land_airplane(self, landing_strip):
        self.landing_data.strip_number = landing_strip
        self.landing_data.actual_time = str(datetime.now().strftime("%d.%m.%y %H:%M:%S"))
        self.__aircraft_status = Flight.status[1]

    def park_airplane(self, parking_spot):
        self.__parking_spot = parking_spot
        self.__aircraft_status = Flight.status[2]

    def plan_start(self, starting_strip):
        self.starting_data.strip_number = starting_strip
        self.__aircraft_status = Flight.status[3]

    def start_airplane(self):
        self.starting_data.actual_time = str(datetime.now().strftime("%d.%m.%y %H:%M:%S"))
        self.__aircraft_status = Flight.status[4]

    @property
    def flight_number(self):
        return self.__flight_number

    @property
    def aircraft_status(self):
        return self.__aircraft_status

