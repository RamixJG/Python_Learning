from datetime import datetime

# Create datetime strings
dst1 = "2020-07-21"
dst2 = "2020-12-31"

# Create date objects from strings
dt1 = datetime.strptime(dst1,"%Y-%m-%d")
dt2 = datetime.strptime(dst2,"%Y-%m-%d")

# Calculate days difference and print
diff = (dt2-dt1).days

print(f"Number of days: {diff}")