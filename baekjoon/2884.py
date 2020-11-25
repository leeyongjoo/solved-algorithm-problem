# 2884: 알람 시계
# https://www.acmicpc.net/problem/2884

h, m = (int(a) for a in input().split(' '))
m -= 45
if m < 0:
    h -= 1
    m += 60
if h < 0:
    h += 24
print(f'{h} {m}')