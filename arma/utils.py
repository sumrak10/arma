import datetime
import random
import string

import pytz

from .settings import TIME_ZONE, START_TIME_AT_THE_COMPANY, END_TIME_AT_THE_COMPANY

def company_working_now() -> bool:
    tz = pytz.timezone(TIME_ZONE)
    now = datetime.datetime.now(tz=tz).time()
    if START_TIME_AT_THE_COMPANY < now < END_TIME_AT_THE_COMPANY:
        work_time = True
    else:
        work_time = False
    return work_time


def get_random_string(length):
    letters = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str