# import datetime
# start = "00:00:00"
# end = "23:59:00"
# delta = datetime.timedelta(minutes=15)
# start = datetime.datetime.strptime( start, '%H:%M:%S' )
# end = datetime.datetime.strptime( end, '%H:%M:%S' )
# t = start
# timestamps = []
# while t <= end :
#      timestamps.append(datetime.datetime.strftime( t, '%H:%M:%S'))
#      t += delta
# print(timestamps)



from datetime import datetime, timedelta

def datetime_range(start, end, delta):
    current = start
    while current < end:
        yield current
        current += delta

dts = [dt.strftime('%Y-%m-%d %H:%M:%S') for dt in 
       datetime_range(datetime(2022, 9, 21, 0), datetime(2022, 9, 21+2, 00), 
       timedelta(minutes=15))]

for d in dts:
    print(d.split()[0] + ", " + d.split()[1])