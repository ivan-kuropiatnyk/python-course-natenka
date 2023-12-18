# -*- coding: utf-8 -*-
import time
from time import strptime


local_time = time.localtime()
#time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
timec = f"{local_time.tm_year}-{local_time.tm_mon}-{local_time.tm_mday} {local_time.tm_hour}:{local_time.tm_min}:{local_time.tm_sec}"
time_string1 = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
time_string2 = time.strptime(timec, "%Y-%m-%d %H:%M:%S") #("%Y-%m-%d %H:%M:%S", local_time)
print("Local time:", local_time)
print("Local time:", timec)
print("YYYY-MM-DD HH:MM:SS => ",
      f"{local_time.tm_year}-{local_time.tm_mon}-{local_time.tm_mday} "
      f"{local_time.tm_hour}:{local_time.tm_min}:{local_time.tm_sec}")
print(time_string1)
print(time_string2)

time_string3_string = '2023-11-21 20:56:00'
time_string3_structured = time.strptime(time_string3_string, "%Y-%m-%d %H:%M:%S")

from datetime import datetime, timedelta
#difference = datetime(0,0,10,0,0,0)
datetime_current = datetime.now()
datetime_old = datetime.strptime(time_string3_string, "%Y-%m-%d %H:%M:%S")
#Statements
print(datetime_current)
print(datetime_old)
print(datetime_current-datetime_old)
difference = datetime_current.timestamp()-datetime_old.timestamp()
print(difference)
dt = datetime.fromtimestamp(difference)
print(dt)
print(604826.8550479412-26.855048)
if difference >= 604800:
      t_s = 604800# 7 days, 0:00:00
      print("This difference is more than 7 days")
      print(datetime.fromtimestamp(604800))
      td = timedelta(seconds=t_s)
      print('Time in Days, hh:mm:ss.ms:', td)

def del_non_act(db_filename):
      connection = sqlite3.connect(db_filename)
      query_0 = "select time_con from dhcp where active='0'"
      result_0 = connection.execute(query_0)
      for time_con in result_0:
            datetime_current = datetime.now()
            datetime_difference = datetime_current.timestamp()-time_con.timestamp()
            if datetime_difference >= 604800:
                  query_info = "select time_con from dhcp where active='0'"
                  result_info = connection.execute(query_info)
                  print("The next data will be deleted=>", result_info)
                  query_del = f"DELETE from dhcp WHERE time_con = '{time_con}';"
                  connection.execute(query_del)
      connection.commit()
      connection.close()