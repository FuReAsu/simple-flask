import time
import datetime

_start_time: float = time.monotonic()

def uptime_seconds() -> float:
    return time.monotonic() - _start_time

def uptime() -> datetime.timedelta:
    return datetime.timedelta(seconds=uptime_seconds())
