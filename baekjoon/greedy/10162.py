# 10162: 전자레인지
# https://www.acmicpc.net/problem/10162

t = int(input())

# a, b, c -> 300, 60, 10
a = t // 300
t %= 300
b = t // 60
t %= 60
c = t // 10
t %= 10

print(f'{a} {b} {c}' if t == 0 else -1)