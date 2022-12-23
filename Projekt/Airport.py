from Projekt.Flight import Flight


class Airport:
    def __init__(self):
        self.landing_strips: list[Tupel(landing_strip, status)]
        self.parking_spots: list[Tupel(parking_spot, status)]
        self.airlines: list[str]
        self.aircraft_types: list[str]
        self.flights: list[Flight]
