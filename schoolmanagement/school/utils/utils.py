from datetime import datetime
import pytz
from school.utils.constants import TIMEZONE

tz = pytz.timezone(TIMEZONE)


class Utils:
    def __init__(self):
        pass

    def get_timestamp(self):
        return datetime.now(tz)
