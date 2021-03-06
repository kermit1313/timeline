from datetime import datetime, timedelta


class Task:
    def __init__(self, duration, resource):
        self.duration = duration
        self.resource = resource
        splitted = resource.split(".")
        self._index = splitted[0]
        self._order = splitted[1]
        self._station_symbol = splitted[2]
        self._start_date_time = None  # type: datetime
        self._end_date_time = None  # type: datetime

    @property
    def station_symbol(self):
        return self._station_symbol

    @property
    def order(self):
        return int(self._order)

    @property
    def index(self):
        return self._index

    @property
    def start_date_time(self):
        return self._start_date_time

    @property
    def end_date_time(self):
        return self._end_date_time

    def set_times(self, start_date_time):
        self._start_date_time = start_date_time
        self._end_date_time = start_date_time + timedelta(hours=self.duration)
