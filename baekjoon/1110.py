# 1110: 더하기 사이클
# https://www.acmicpc.net/problem/1110

n = int(input())
new = n
time = 0
while True:
    time += 1
    x, y = new // 10, new % 10
    new = (y * 10) + (x + y) % 10
    if new == n:
        break
print(time)
