# 2525: 오븐 시계
# https://www.acmicpc.net/problem/2525

a, b = map(int, input().split())
c = int(input())

b += c
if b >= 60:
    a += b // 60
    b %= 60

if a >= 24:
    a %= 24
print(a, b)
