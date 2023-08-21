import datetime
from dateutil import parser

now = datetime.datetime.today()

trial_date = '2023-08-20T10:24'
actual_date = parser.parse(trial_date)
print(actual_date)
print(now)
print(now > actual_date)