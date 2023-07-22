import datetime as dt
from datetime import datetime, timedelta

# Setting beginning date, ending date and timedelta
dtb = dt.datetime(2020,1,1)
dte = dt.datetime(2020,1,4,16)
td = timedelta(hours=8)
dates = [dtb]

while dtb != dte:
    dtb += td
    dates.append(dtb) 

for date in dates:
    print(date)