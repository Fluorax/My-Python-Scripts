#!/usr/bin/env python
#This script is used to insert new values to the 'Personal Log' DB. 

import time, sys, psycopg2

def chems_updater():
    con = psycopg2.connect(database="DB_NAME_GOES_HERE", user="USER_NAME_GOES_HERE", password="PWD_GOES_HERE", host="HOST_IP_GOES_HERE", port="PORT_GOES_HERE") 
    print("Database opened successfully!")
    print('Please complete the following fields:')
    Supplement=input('COMPOUND:')
    quantity=input('MASS:')
    unit=input('UNIT OF MEASUREMENT:')

    cur = con.cursor()

    cur.execute("INSERT INTO TABLE_NAME_GOES_HERE (COLUMN_1, COLUMN_2, COLUNT_3) VALUES (%s,%s,%s)", ((Supplement),(unit),(quantity)))

    con.commit()
    print("Record inserted successfully!")
    con.close()

def sleep_updater():
    con = psycopg2.connect(database="DB_NAME_GOES_HERE", user="USER_NAME_GOES_HERE", password="PWD_GOES_HERE", host="HOST_IP_GOES_HERE", port="PORT_GOES_HERE")
    print("Database opened successfully!")
    print('Format for DATE is DD-MM-YY and TIME HH:MM:SS. Time inputs can also be in this format HH:MM')
    date1=input('DATE:')
    total1=input('TOTAL SLEEP TIME:')
    deep1=input('DEEP SLEEP TIME:')

    cur = con.cursor()

    cur.execute("INSERT INTO SLEEP (date, total, deep) VALUES (%s,%s,%s)", ((date1),(total1),(deep1)))

    con.commit()
    print("Record inserted successfully!")
    con.close()

while True:

    print('Press 1 to update your supplement log, 2 to update your sleep log or 3 to exit.')
    selection=int(input())
    

    if selection == 1:
        chems_updater()

    elif selection == 2:
        sleep_updater()

    elif selection == 3:
        print('Have a nice day!')
        time.sleep(2)
        sys.exit()
        
    else:
        continue
    
