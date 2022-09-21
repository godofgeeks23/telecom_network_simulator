import csv
from datetime import date, datetime, timedelta
# from datetime import datetime
from random import randrange

attributes = ["tower", "date", "time", 
"tower_a", "tower_a_ue_count", "tower_a_utilization", "tower_a_signaling_load",
"tower_b", "tower_b_ue_count", "tower_b_utilization", "tower_b_signaling_load",
"tower_c", "tower_c_ue_count", "tower_c_utilization", "tower_c_signaling_load"
]

start_time = datetime.strptime("00:00:00", "%H:%M:%S")
end_time = datetime.strptime("23:59:00", "%H:%M:%S")
time_gap = 15
time_stamps = [(start_time + timedelta(hours=time_gap*i/60)).strftime("%H:%M:%S")
       for i in range(int((end_time-start_time).total_seconds() / 60.0 / time_gap))]

with open('generated_data.csv', 'w') as f:
    write = csv.writer(f)
      
    write.writerow(attributes)

    for timestamp in time_stamps:

        tower_name = "ramnagar"
        current_date = date.today()

        # now = datetime.now()
        # current_time = now.strftime("%H:%M:%S")
        current_time = timestamp

        tower_a = tower_name + "_a"
        tower_b = tower_name + "_b"
        tower_c = tower_name + "_c"

        tower_a_ue_count = randrange(300)
        tower_b_ue_count = randrange(300)
        tower_c_ue_count = randrange(300)

        tower_a_util = randrange(100)
        tower_b_util = randrange(100)
        tower_c_util = randrange(100)
        
        tower_a_sig_load = randrange(100)
        tower_b_sig_load = randrange(100)
        tower_c_sig_load = randrange(100)

        data_row = []
        data_row.append(tower_name)
        data_row.append(current_date)
        data_row.append(current_time)
        data_row.append(tower_a)
        data_row.append(tower_a_ue_count)
        data_row.append(tower_a_util)
        data_row.append(tower_a_sig_load)
        data_row.append(tower_b)
        data_row.append(tower_b_ue_count)
        data_row.append(tower_b_util)
        data_row.append(tower_b_sig_load)
        data_row.append(tower_c)
        data_row.append(tower_c_ue_count)
        data_row.append(tower_c_util)
        data_row.append(tower_c_sig_load)
        
        write.writerow(data_row)


