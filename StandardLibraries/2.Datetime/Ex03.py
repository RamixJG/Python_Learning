from datetime import datetime

# Create datetime strings
dst1 = "12:00:00"
dst2 = "6:30:00"
dst3 = "9:15:00"

# Create date objects from strings
dt1 = datetime.strptime(dst1,"%H:%M:%S")
dt2 = datetime.strptime(dst2,"%H:%M:%S")
dt3 = datetime.strptime(dst3,"%H:%M:%S")

# Format in order to print only the time
dt = [dt1,dt2,dt3]
d = []
for idx, datime in enumerate(dt,1):
    d.append(datime.strftime("%H:%M:%S"))
    print(d[idx-1])