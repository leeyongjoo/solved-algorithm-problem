# 2753: 윤년
# https://www.acmicpc.net/problem/2753

a = int(input())
print(1 if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0) else 0)