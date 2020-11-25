# 10952: A+B - 5
# https://www.acmicpc.net/problem/10952

while True:
    a, b = map(int, input().split(' '))
    ab_sum = a + b
    if ab_sum:
        print(ab_sum)
    else:
        break
