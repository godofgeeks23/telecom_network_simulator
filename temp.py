import csv
from datetime import date, datetime, timedelta
# from datetime import datetime
from random import randrange

start = datetime.strptime("00:00:00", "%H:%M:%S")
end = datetime.strptime("23:45:00", "%H:%M:%S")

# min_gap
min_gap = 15

# compute datetime interval
arr = [(start + timedelta(hours=min_gap*i/60)).strftime("%H:%M:%S")
       for i in range(int((end-start).total_seconds() / 60.0 / min_gap))]
print(arr)
