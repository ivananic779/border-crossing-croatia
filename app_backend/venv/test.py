from time import time
from db import connect_database
import time

conn = connect_database()

conn.execute("SELECT DATEADD(dd, 0, DATEDIFF(dd, 0, date)) as name, ulaz_ukupno as value FROM t_ukupno")

for date, value in conn.fetchall():
    print(date)
    print(value)
    
    # Convert date to day-month-year format
    date_str = date.strftime("%d-%m-%Y")
    print(date_str)
    time.sleep(10)