# 18301: Rats
# https://www.acmicpc.net/problem/18301

n1, n2, n12 = map(int, input().split())
print((n1 + 1) * (n2 + 1) // (n12 + 1) - 1)