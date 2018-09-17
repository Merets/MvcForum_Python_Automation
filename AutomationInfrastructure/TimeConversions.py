import datetime


class TimeConversions(object):
    @classmethod
    def add_time(cls, time_a, time_b):
        return time_a + datetime.timedelta(hours=time_b.hour, minutes=time_b.minute, seconds=time_b.second,
                                           microseconds=time_b.microsecond)
