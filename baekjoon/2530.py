# 2530: 인공지능 시계
# https://www.acmicpc.net/problem/2530

a, b, c = map(int, input().split())
d = int(input())

c += d
if c >= 60:
    b += c // 60
    c %= 60

if b >= 60:
    a += b // 60
    b %= 60

if a >= 24:
    a %= 24
print(a, b, c)
