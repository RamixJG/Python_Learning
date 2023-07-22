from datetime import datetime

# Create datetime strings
dst1 = "2021-01-01"
dst2 = "31/7/21"
dst3 = "May 7, 1990"

# Create date objects from strings
dt1 = datetime.strptime(dst1,"%Y-%m-%d")
dt2 = datetime.strptime(dst2,"%d/%m/%y")
dt3 = datetime.strptime(dst3,"%b %d, %Y")

# Format in order to print only the date 
dt = [dt1,dt2,dt3]
d = []
for idx, datime in enumerate(dt,1):
    d.append(datime.strftime("%Y-%m-%d"))
    print(d[idx-1])































































































