# 2588: 곱셈
# https://www.acmicpc.net/problem/2588

a, b = (input() for _ in range(2))
a = int(a)
for i, s in enumerate(b[::-1]):
    print(a * int(s))
print(a * int(b))