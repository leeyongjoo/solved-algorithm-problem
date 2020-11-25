# 14681: 사분면 고르기
# https://www.acmicpc.net/problem/14681

x, y = (int(input()) for _ in range(2))

if x > 0:
    if y > 0:
        print(1)
    elif y < 0:
        print(4)
elif x < 0:
    if y > 0:
        print(2)
    elif y < 0:
        print(3)