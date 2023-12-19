import time

local_time = time.localtime()

time = f"{local_time.tm_year}-{local_time.tm_mon}-{local_time.tm_mday} {local_time.tm_hour}:{local_time.tm_min}:{local_time.tm_sec}"

print("Local time:", local_time)
print("Local time:", time)
print("YYYY-MM-DD HH:MM:SS => ",
      f"{local_time.tm_year}-{local_time.tm_mon}-{local_time.tm_mday} "
      f"{local_time.tm_hour}:{local_time.tm_min}:{local_time.tm_sec}")