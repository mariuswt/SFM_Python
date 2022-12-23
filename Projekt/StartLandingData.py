from datetime import datetime


class StartLandingData:
    def __init__(self, scheduled_time="00.00.00 00:00:00", actual_time="00.00.00 00:00:00", strip_number=0):
        self.format_data = "%d.%m.%y %H:%M:%S"
        self.__scheduled_time: datetime = datetime.strptime(scheduled_time, self.format_data)
        self.__actual_time: datetime = datetime.strptime(actual_time, self.format_data)
        self.__strip_number: int = strip_number

    @property
    def scheduled_time(self):
        return self.__scheduled_time

    @scheduled_time.setter
    def scheduled_time(self, date_time):
        self.__scheduled_time = datetime.strptime(date_time, self.format_data)

    @property
    def actual_time(self):
        return self.__actual_time

    @actual_time.setter
    def actual_time(self, date_time):
        self.__actual_time = datetime.strptime(date_time, self.format_data)

    @property
    def strip_number(self):
        return self.__strip_number

    @strip_number.setter
    def strip_number(self, value):
        self.__strip_number = value


