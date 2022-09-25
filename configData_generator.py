import csv
# import datetime
from random import randrange
from datetime import datetime, timedelta

attributes = ["tower", 
"tower_a", "tx_power_a", "electrical_tilt_a", "cell_onoff_a",
"tower_b", "tx_power_b", "electrical_tilt_b", "cell_onoff_b",
"tower_c", "tx_power_c", "electrical_tilt_c", "cell_onoff_c",
"lat", "long", "site_mode", "azimuth_a", "azimuth_b", "azimuth_c"
]

locations = ["Abupur","Achheja","Adhyatmic Nagar","Alamnagar","Alipur","Alttc","Anwarpur","Arya Nagar","Asaura","Ashok Nagar","Athsaini","Atola","Ator Nagla","Atrauli","Aurangabad Ristal","B.B.nagar","Babugarh","Bachhlota","Badshahnpur Siroli","Bagarpur","Bahadurgarh","Bajhera Kalan","Bajhera Khurd","Bankhanda","Basantpur Sainthli","Baxur","Begmabad","Behta Hazipur","Bhadauli","Bhadoli","Bhadsiyana","Bhaina Dholpur","Bharat Nagar","Bharna","Bhatiyana","Bhikanpur","Bhojpur","Bhup Kheri","Bihuni","Biraj Ghat","Chajarsi","Chamri","Chander Nagar","Chaupla","Chhajupur","Chhaprola","Chhipyana","Chikamberpur","Chrori","Churiyala","Dadri","Dahana","Dasna","Dasna Gate ed","Dasna R.s.","Datiyana","Dehpa Azampur","Dehra Rampur","Delhi Road","Dhana","Dhanaura","Dhara","Dhaulana","Didoli","Doohri","Dosa Bangerpur","Dotai","Duhai","Dundahara","Farid Nagar","Farrukh Nagar","Galand","Gandu Nagla","Garh Town","Garhmukteswar","Ghaziabad","Ghaziabad City","Ghungrala","Girdharpur Tmrel","Gohrs Alamgirpur","Govindpuram","Govindpuri","Gyan Lok","Gyaspur","Haidarpur","Hapur","Hapur Mandi","Harmukhpuri","Harsinghpur","Hasanpur Bhowapur","Hassanpur","Hindan Nagar","Hindon Air field","Hosdarpur","I.E.hapur","I.E.sahibabad","Iklahdi","Ingram Institute","Jakhera Rahmatpur","Jalalabad","Jalalpur Dhindar","Jaoli","Jharina","Jindal Nagar","Kaila","Kakra","Kalchina","Kamla Nehru nagar","Kanauja","Kandaula","Kanya Kalyanpur","Kastala","Kathikhera","Kaushambi","Kavi Nagar","Khanjarpur","Kharkhari","Khera","Khiluai","Khimawati","Khindora","Kishan Ganj","Kumhera","Kushlia","Loni","Luhari","Madarsa Sadat","Mahendrapuri","Mahmoodpur","Mahmoodpur Palwara","Makanpur","Mandola","Mathurawali","Matnaurs","Meerut Road","Model Town","Modi Nagar","Modipon","Mohan Nagar","Mohd. pur khudaliya","Morta","Mubarikpur","Mukeempur","Murad Nagar","Murad Nagar bazar","Murad Nagar town","Muradpur Janupura","Nagla Akhu","Nagola","Nahal","Nali Husainpur","Nan","Nanpur","Nasratpura","Nehru Nagar","Nek Nanpur nanai","Nekpur","New Market pilkhauwa","New Raj nagar","Nistoli","Niwari","Noorpur","Old Raj nagar","Painga","Parpa","Pasonda","Patla","Phagota","Phuldehra","Pilkhauwa Post office","Police Line harsaon","Postal Staff college (i)","Raghunathpur","Raispur","Rajapur","Rajethi","Rampur Puth","Ramte Ram road","Raoli Kalan","Rasulpur","Rewri Rewra","Rly Road hapur","Rori","Roza Yakubpur","Sadarpur","Sadullapur","Sahibabad","Saidpur","Sakhpur","Salarpur","Samaipur","Samana","Sapnawat","Sara","Saunda","Sec-27 Noida","Sec-41 Noida","Shah Mohiuddinpur","Shahjahanpur","Shahpur","Shahpur Bamheta","Shalimar Bagh","Sharpur","Shyampur Jatt","Sikandarpur Kakori","Sikhera","Sikri Kalan","Sikri Khurd","Simbhaoli","Solana","Sultanpur","Surana","Surya Nagar","Talhata","Tatarpur","Teela Sahbazpur","Tibra","Tyori","Udai Rampur nagla","Upera","Vasundhra","Vijai Nagar"]

site_modes = ["coverage", "capacity"]

with open('config_data.csv', 'w') as f:
    write = csv.writer(f)
      
    write.writerow(attributes)

    for location in locations:

        lat = randrange(5, 240)
        long = randrange(5, 240)

        for sitemode in site_modes:

            tower_name = location

            tower_a = tower_name + "_a"
            tower_b = tower_name + "_b"
            tower_c = tower_name + "_c"

            tx_power_a = randrange(20, 70)
            tx_power_b = randrange(20, 70)
            tx_power_c = randrange(20, 70)

            electrical_tilt_a = randrange(10)
            electrical_tilt_b = randrange(10)
            electrical_tilt_c = randrange(10)

            cell_onoff_a = "on"
            cell_onoff_b = "on"
            cell_onoff_c = "on"

            site_mode = sitemode

            azimuth_a = randrange(0,360,30)
            azimuth_b = randrange(0,360,30)
            azimuth_c = randrange(0,360,30)

            data_row = []
            data_row.append(tower_name)

            data_row.append(tower_a)
            data_row.append(tx_power_a)
            data_row.append(electrical_tilt_a)
            data_row.append(cell_onoff_a)
            
            data_row.append(tower_b)
            data_row.append(tx_power_b)
            data_row.append(electrical_tilt_b)
            data_row.append(cell_onoff_b)

            data_row.append(tower_c)
            data_row.append(tx_power_c)
            data_row.append(electrical_tilt_c)
            data_row.append(cell_onoff_c)

            data_row.append(lat)
            data_row.append(long)
            data_row.append(site_mode)
            data_row.append(azimuth_a)
            data_row.append(azimuth_b)
            data_row.append(azimuth_c)
            
            write.writerow(data_row)
