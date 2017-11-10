# -*- coding: utf8 -*-

import datetime
import pytz

time_zone = pytz.timezone('Asia/Shanghai')

# get naive date
date = datetime.datetime.now().date()
# get naive time
time = datetime.time(12, 30)
# combite to datetime
date_time = datetime.datetime.combine(date, time)
# make time zone aware
date_time = time_zone.localize(date_time)

# convert to UTC
utc_date_time = date_time.astimezone(pytz.utc)
# get time
utc_time = utc_date_time.time()

print(date_time)
print(utc_date_time)
print(utc_time)