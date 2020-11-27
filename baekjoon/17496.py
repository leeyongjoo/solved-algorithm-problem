# 17496: 스타후르츠
# https://www.acmicpc.net/problem/17496

n, t, c, p = map(int, input().split())
print(((n - 1) // t) * c * p)