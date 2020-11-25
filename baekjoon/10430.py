# 10430: 나머지
# https://www.acmicpc.net/problem/10430

A, B, C = (int(a) for a in input().split(' '))
print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)