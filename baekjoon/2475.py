# 2475: 검증수
# https://www.acmicpc.net/problem/2475

print(sum(map(lambda x: x ** 2, map(int, input().split()))) % 10)