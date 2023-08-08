from datetime import datetime

# Create datetime strings
dst1 = "Jul 20 2020 11:30:00"
dst2 = "1990-03-10 12:00:00"
dst3 = "2021-01-01 00:00:00"

# Create date objects from strings
dt1 = datetime.strptime(dst1,"%b %d %Y %H:%M:%S")
dt2 = datetime.strptime(dst2,"%Y-%m-%d %H:%M:%S")
dt3 = datetime.strptime(dst3,"%Y-%m-%d %H:%M:%S")

# Print dates 
dt = [dt1,dt2,dt3]
for date in dt:
    print(date)