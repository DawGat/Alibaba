import datetime
from suntime import Sun, SunTimeException
from globals import Global
import datetime


class TimeRange:
    def __init__(self, start_hour, start_minute, end_hour, end_minute, start_sun=None, end_sun=None):
        self.start_hour = start_hour
        self.start_minute = start_minute
        self.end_hour = end_hour
        self.end_minute = end_minute
        self.start_sun = start_sun
        self.end_sun = end_sun
        self.start_time = None
        self.end_time = None

    # Set the start and end time for time range within switch should be turned on
    def set_time_range(self):
        self.start_time = datetime.time(hour=self.start_hour, minute=self.start_minute)
        self.end_time = datetime.time(hour=self.end_hour, minute=self.end_minute)
        print('Start time set to: %s\nEnd time set to: %s' % (self.start_time, self.end_time))

    # Return TRUE when actual time is in time range
    def is_in_time_range(self):
        time_now = datetime.datetime.now().time()
        if self.start_time <= self.end_time:
            return self.start_time <= time_now <= self.end_time
        else:
            return self.start_time <= time_now or time_now <= self.end_time


def get_sun_day():
    position = Sun(Global.position['latitude'], Global.position['longitude'])
    sun_day = dict()
    sun_day['sunrise'] = position.get_local_sunrise_time().strftime('%H:%M')
    sun_day['sunset'] = position.get_local_sunset_time().strftime('%H:%M')
    print('Today sun rise at: %s \nToday sun set at: %s' % (sun_day['sunrise'], sun_day['sunset']))
    return sun_day
