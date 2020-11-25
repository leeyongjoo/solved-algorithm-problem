# 2845: 파티가 끝나고 난 뒤
# https://www.acmicpc.net/problem/2845

l, p = map(int, input().split())
party = l * p
print(' '.join(map(str, map(lambda x: int(x) - party, input().split()))))