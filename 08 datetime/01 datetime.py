import datetime
import time

x = datetime.datetime.now()
print(x)
# 输出结果：2021-08-10 10:05:14.641351

today = time.localtime(time.time())
year_initial = today[0]
month_initial = today[1]
day_initial = today[2]

print(today)
print(year_initial, month_initial, day_initial)
# 输出为 2021 8 10
