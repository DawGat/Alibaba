import datetime
from suntime import Sun, SunTimeException
from globals import Global
import datetime

sun_relations = {'before_sun_rise': 'bsr', 'after_sun_rise': 'asr', 'before_sun_set': 'bss', 'after_sun_set': 'ass'}

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
        if self.start_sun not in sun_relations.values():
            self.start_time = datetime.time(hour=self.start_hour, minute=self.start_minute)
        else:
            time_delta = datetime.timedelta(hours=self.start_hour, minutes=self.start_minute)
            if self.start_sun == sun_relations['before_sun_set']:
                self.start_time = (Global.sun_set_time - time_delta).time()
            elif self.start_sun == sun_relations['after_sun_set']:
                self.start_time = (Global.sun_set_time + time_delta).time()
            elif self.start_sun == sun_relations['before_sun_rise']:
                self.start_time = (Global.sun_rise_time - time_delta).time()
            elif self.start_sun == sun_relations['after_sun_rise']:
                self.start_time = (Global.sun_rise_time + time_delta).time()

        if self.end_sun not in sun_relations.values():
            self.end_time = datetime.time(hour=self.end_hour, minute=self.end_minute)
        else:
            time_delta = datetime.timedelta(hours=self.end_hour, minutes=self.end_minute)
            if self.end_sun == sun_relations['before_sun_set']:
                self.end_time = (Global.sun_set_time - time_delta).time()
            elif self.end_sun == sun_relations['after_sun_set']:
                self.end_time = (Global.sun_set_time + time_delta).time()
            elif self.end_sun == sun_relations['before_sun_rise']:
                self.end_time = (Global.sun_rise_time - time_delta).time()
            elif self.end_sun == sun_relations['after_sun_rise']:
                self.end_time = (Global.sun_rise_time + time_delta).time()

        print('Start time set to: %s\nEnd time set to: %s' % (self.start_time, self.end_time))

    # Return TRUE when actual time is in time range
    def is_in_time_range(self):
        time_now = datetime.datetime.now().time()
        if self.start_time <= self.end_time:
            return self.start_time <= time_now <= self.end_time
        else:
            return self.start_time <= time_now or time_now <= self.end_time


def set_sun_day():
    position = Sun(Global.position['latitude'], Global.position['longitude'])
    sun_day = dict()
    Global.sun_rise_time = position.get_local_sunrise_time()
    Global.sun_set_time = position.get_local_sunset_time()
    print('Today sun rise at: %s \nToday sun set at: %s' % (Global.sun_rise_time, Global.sun_set_time))
    return sun_day
