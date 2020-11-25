# 2675: 문자열 반복
# https://www.acmicpc.net/problem/2675

t = int(input())
for _ in range(t):
    r, s = input().split(' ')
    for c in s:
        print(c * int(r), end='')
    print()
