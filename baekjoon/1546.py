# 1546: 평균
# https://www.acmicpc.net/problem/1546

n = int(input())
arr = list(map(int, input().split(' ')))
max_arr = max(arr)
arr = [a / max_arr * 100 for a in arr]
print(sum(arr) / n)
