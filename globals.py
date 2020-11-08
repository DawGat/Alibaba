import datetime


class Global(object):
    switches = []
    test_mode = True
    position = {
        'latitude': 00.00,
        'longitude': 00.00
    }
    sun_rise_time = datetime.datetime(2020, 10, 27, 8, 00)
    sun_set_time = datetime.datetime(2020, 10, 27, 21, 00)




