# 16170: 오늘의 날짜는?
# https://www.acmicpc.net/problem/16170

from datetime import datetime
print(datetime.utcnow().year)
print(datetime.utcnow().month)
print(datetime.utcnow().day)