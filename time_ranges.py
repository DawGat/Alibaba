import datetime
from suntime import Sun, SunTimeException
from globals import Global


# Function return True if time (by default current time) is in given time range
def time_in_range(start, end):
    time_now = datetime.datetime.now().time()
    if start <= end:
        return start <= time_now <= end
    else:
        return start <= time_now or time_now <= end


# position = Sun(Global.position['latitude'], Global.position['longitude'])
# today_sunrise = position.get_local_sunrise_time().strftime('%H:%M')
# today_sunset = position.get_local_sunset_time().strftime('%H:%M')
# print(today_sunset, today_sunrise)
