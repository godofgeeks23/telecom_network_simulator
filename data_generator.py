import csv
# import datetime
from random import randrange
from datetime import datetime, timedelta

def datetime_range(start, end, delta):
    current = start
    while current < end:
        yield current
        current += delta

attributes = ["tower", "date", "time", 
"tower_a", "tower_a_ue_count", "tower_a_utilization", "tower_a_signaling_load",
"tower_b", "tower_b_ue_count", "tower_b_utilization", "tower_b_signaling_load",
"tower_c", "tower_c_ue_count", "tower_c_utilization", "tower_c_signaling_load"
]

locations = ["Abupur","Achheja","Adhyatmic Nagar","Alamnagar","Alipur","Alttc","Anwarpur","Arya Nagar","Asaura","Ashok Nagar","Athsaini","Atola","Ator Nagla","Atrauli","Aurangabad Ristal","B.B.nagar","Babugarh","Bachhlota","Badshahnpur Siroli","Bagarpur","Bahadurgarh","Bajhera Kalan","Bajhera Khurd","Bankhanda","Basantpur Sainthli","Baxur","Begmabad","Behta Hazipur","Bhadauli","Bhadoli","Bhadsiyana","Bhaina Dholpur","Bharat Nagar","Bharna","Bhatiyana","Bhikanpur","Bhojpur","Bhup Kheri","Bihuni","Biraj Ghat","Chajarsi","Chamri","Chander Nagar","Chaupla","Chhajupur","Chhaprola","Chhipyana","Chikamberpur","Chrori","Churiyala","Dadri","Dahana","Dasna","Dasna Gate ed","Dasna R.s.","Datiyana","Dehpa Azampur","Dehra Rampur","Delhi Road","Dhana","Dhanaura","Dhara","Dhaulana","Didoli","Doohri","Dosa Bangerpur","Dotai","Duhai","Dundahara","Farid Nagar","Farrukh Nagar","Galand","Gandu Nagla","Garh Town","Garhmukteswar","Ghaziabad","Ghaziabad City","Ghungrala","Girdharpur Tmrel","Gohrs Alamgirpur","Govindpuram","Govindpuri","Gyan Lok","Gyaspur","Haidarpur","Hapur","Hapur Mandi","Harmukhpuri","Harsinghpur","Hasanpur Bhowapur","Hassanpur","Hindan Nagar","Hindon Air field","Hosdarpur","I.E.hapur","I.E.sahibabad","Iklahdi","Ingram Institute","Jakhera Rahmatpur","Jalalabad","Jalalpur Dhindar","Jaoli","Jharina","Jindal Nagar","Kaila","Kakra","Kalchina","Kamla Nehru nagar","Kanauja","Kandaula","Kanya Kalyanpur","Kastala","Kathikhera","Kaushambi","Kavi Nagar","Khanjarpur","Kharkhari","Khera","Khiluai","Khimawati","Khindora","Kishan Ganj","Kumhera","Kushlia","Loni","Luhari","Madarsa Sadat","Mahendrapuri","Mahmoodpur","Mahmoodpur Palwara","Makanpur","Mandola","Mathurawali","Matnaurs","Meerut Road","Model Town","Modi Nagar","Modipon","Mohan Nagar","Mohd. pur khudaliya","Morta","Mubarikpur","Mukeempur","Murad Nagar","Murad Nagar bazar","Murad Nagar town","Muradpur Janupura","Nagla Akhu","Nagola","Nahal","Nali Husainpur","Nan","Nanpur","Nasratpura","Nehru Nagar","Nek Nanpur nanai","Nekpur","New Market pilkhauwa","New Raj nagar","Nistoli","Niwari","Noorpur","Old Raj nagar","Painga","Parpa","Pasonda","Patla","Phagota","Phuldehra","Pilkhauwa Post office","Police Line harsaon","Postal Staff college (i)","Raghunathpur","Raispur","Rajapur","Rajethi","Rampur Puth","Ramte Ram road","Raoli Kalan","Rasulpur","Rewri Rewra","Rly Road hapur","Rori","Roza Yakubpur","Sadarpur","Sadullapur","Sahibabad","Saidpur","Sakhpur","Salarpur","Samaipur","Samana","Sapnawat","Sara","Saunda","Sec-27 Noida","Sec-41 Noida","Shah Mohiuddinpur","Shahjahanpur","Shahpur","Shahpur Bamheta","Shalimar Bagh","Sharpur","Shyampur Jatt","Sikandarpur Kakori","Sikhera","Sikri Kalan","Sikri Khurd","Simbhaoli","Solana","Sultanpur","Surana","Surya Nagar","Talhata","Tatarpur","Teela Sahbazpur","Tibra","Tyori","Udai Rampur nagla","Upera","Vasundhra","Vijai Nagar"]

extended_timestamps = [dt.strftime('%Y-%m-%d %H:%M:%S') for dt in 
       datetime_range(datetime(2022, 9, 21, 0), datetime(2022, 9, 21+2, 00), 
       timedelta(minutes=1))]


with open('generated_data.csv', 'w') as f:
    write = csv.writer(f)
      
    write.writerow(attributes)

    for timestamp in extended_timestamps:

        for location in locations:

            tower_name = location

            current_date = timestamp.split()[0]

            current_time = timestamp.split()[1]

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
