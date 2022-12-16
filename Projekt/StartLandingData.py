import datetime


class StartLandingData:
    def __init__(self):
        self.scheduled_time: datetime.datetime
        self.actual_time: datetime.datetime
        self.strip_number: int = 0
