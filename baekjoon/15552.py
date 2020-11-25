# 15552: 빠른 A+B
# https://www.acmicpc.net/problem/15552

import sys
n = int(input())
for _ in range(n):
    print(sum(map(int, sys.stdin.readline().rstrip().split(' '))))