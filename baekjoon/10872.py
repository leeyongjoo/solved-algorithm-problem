# 10872: 팩토리얼
# https://www.acmicpc.net/problem/10872

N = int(input())

def fac(n):
    if n == 1: return 1
    elif n == 0: return 1
    return n * fac(n-1)

print(fac(N))