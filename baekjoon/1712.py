# 1712: 손익분기점
# https://www.acmicpc.net/problem/1712

a, b, c = map(int, input().split())
if c - b > 0:
    result = a // (c - b) + 1
    print(result if result > 0 else -1)
else:
    print(-1)