from datetime import datetime

# Create datetime strings
dst1 = "Jul 20 2020 11:30:00"
dst2 = "2021-02-20 10:25:00"

# Create date objects from strings
dt1 = datetime.strptime(dst1,"%b %d %Y %H:%M:%S")
dt2 = datetime.strptime(dst2,"%Y-%m-%d %H:%M:%S")

# Calculate time difference between the dates and print
diff = dt2-dt1

print(diff)