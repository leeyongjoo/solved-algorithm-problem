# 8958: OX퀴즈
# https://www.acmicpc.net/problem/8958

n = int(input())
for _ in range(n):
    arr = input()
    cur = 0
    cnt = 0
    for a in arr:
        if a == 'O':
            cur += 1
            cnt += cur
        else:
            cur = 0
    print(cnt)
