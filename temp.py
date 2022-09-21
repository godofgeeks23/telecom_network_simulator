import datetime
start = "00:00:00"
end = "23:59:00"
delta = datetime.timedelta(minutes=15)
start = datetime.datetime.strptime( start, '%H:%M:%S' )
end = datetime.datetime.strptime( end, '%H:%M:%S' )
t = start
timestamps = []
while t <= end :
     timestamps.append(datetime.datetime.strftime( t, '%H:%M:%S'))
     t += delta
print(timestamps)