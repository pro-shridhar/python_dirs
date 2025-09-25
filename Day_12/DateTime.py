from datetime import datetime, time, timedelta

current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(current_datetime)

tem = datetime.now()
print(tem)

date_string = "2025-09-18 14:30:15"
date_object = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(date_object)

time1 = time(12, 11, 25)
date1 = datetime(2012, 12, 24)
print(date1)
print(datetime.now() + timedelta(days=365))  # date afer 365 days
