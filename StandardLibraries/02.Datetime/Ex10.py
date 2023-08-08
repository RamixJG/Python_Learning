import datetime as dt
from datetime import datetime

new_year = dt.datetime(2024,1,1)

# Days difference
diff =new_year-datetime.now()

# Print number of days 
print(f'Until the end of the year: {diff}')