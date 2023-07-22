from datetime import datetime

# Date to format

dst = "2021-04-20 11:30:00"
dt = datetime.strptime(dst,"%Y-%m-%d %H:%M:%S")

# Different date format types
dt1 = datetime.strftime(dt,"%Y-%m-%d")
dt2 = datetime.strftime(dt,"%d-%m-%Y")
dt3 = datetime.strftime(dt,"%m-%Y")
dt4 = datetime.strftime(dt,"%B-%Y")
dt5 = datetime.strftime(dt,"%d %B, %Y")
dt6 = dt
dt7 = datetime.strftime(dt,"%m/%d/%y %H:%M:%S")
dt8 = datetime.strftime(dt,"%d(%a) %B %Y")

for i in range(1,9):
    print(locals()[f"dt{i}"])