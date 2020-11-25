# 4344: 평균은 넘겠지
# https://www.acmicpc.net/problem/4344

c = int(input())
for _ in range(c):
    n, *arr = map(int, input().split(' '))
    avg = sum(arr) / n
    print(f'{len(list(filter(lambda x: x > avg, arr))) / n * 100:.3f}%')
