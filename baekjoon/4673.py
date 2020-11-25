# 4673: 셀프 넘버
# https://www.acmicpc.net/problem/4673

max_limit = 10000
self_numbers = [False] + [True] * max_limit

for i in range(1, max_limit + 1):
    n = i
    n += sum(map(int, str(n)))
    if n <= max_limit:
        self_numbers[n] = False

    if self_numbers[i]:
        print(i)
