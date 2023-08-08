import datetime as dt
from datetime import datetime, timedelta

# Setting initial date
date = dt.datetime(2020,1,1)

# Shifting by the desired deltas and print
dt1 = date + timedelta(days=7)
dt2 = date + timedelta(days=30)
dt3 = date + timedelta(hours=30)
dt4 = date + timedelta(minutes=15)

for i in range(1,5):
    print(locals()[f"dt{i}"])