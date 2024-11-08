import datetime
import time

class TimeMeasurer(object):
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if(self._initialized): return
        self._initialized = True
        self._timers_list = []

    def appendTimersList(self, timerTuple):
        self._timers_list.append(timerTuple)

    def getTimersList(self):
        return self._timers_list

class ScopeMeasurer(object):
    def __init__(self, description):
        self.tm = TimeMeasurer()
        self.description = description
        self.start = 0

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exception_type, exception_value, traceback):
        end = time.time()
        duration = end - self.start
        self.tm.appendTimersList((self.description, duration))

def PrintTimers():
    timers = TimeMeasurer().getTimersList()
    for timer in timers:
        desc, dur = timer
        print("{}: {} s == {}".format(desc, dur, datetime.timedelta(seconds=dur)))
