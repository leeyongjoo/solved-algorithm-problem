# 10871: X보다 작은 수
# https://www.acmicpc.net/problem/10871

n, x = map(int, input().split(' '))
arr_less_than_x = list(map(str, filter(lambda a: a < x, map(int, input().split(' ')))))
print(' '.join(arr_less_than_x))
