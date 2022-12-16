from Projekt.StartLandingData import StartLandingData


class Flight:
    def __init__(self, airline, aircraft_type):
        self.airline = airline
        self.aircraft_type = aircraft_type
        self.flight_number: str = ""
        self.landing_data: StartLandingData
        self.starting_data: StartLandingData
        self.parking_spot: int = 0


