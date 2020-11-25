# 3003: 킹, 퀸, 룩, 비숍, 나이트, 폰
# https://www.acmicpc.net/problem/3003

pieces = [1, 1, 2, 2, 2, 8]
print(*[a - int(b) for a, b in zip(pieces, input().split())])
