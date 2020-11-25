# 2562: 최댓값
# https://www.acmicpc.net/problem/2562

arr = sorted([(int(input()), i + 1) for i in range(9)])
print(arr[-1][0])
print(arr[-1][1])
