import datetime


# Function return True if time (by default current time) is in given time range
def time_in_range(start, end):
    time_now = datetime.datetime.now().time()
    if start <= end:
        return start <= time_now <= end
    else:
        return start <= time_now or time_now <= end

