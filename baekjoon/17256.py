# 17256: 달달함이 넘쳐흘러
# https://www.acmicpc.net/problem/17256

ax, ay, az = map(int, input().split())
cx, cy, cz = map(int, input().split())
print(cx - az, cy // ay, cz - ax)