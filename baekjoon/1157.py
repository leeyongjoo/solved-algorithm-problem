# 1157: 단어 공부
# https://www.acmicpc.net/problem/1157

from collections import defaultdict

s = input()
if len(s) < 2:
    print(s.upper())
else:
    dd = defaultdict(int)
    for c in s.lower():
        dd[c] += 1
    items = sorted(dd.items(), key=lambda x: x[1])
    if items[-1][1] == items[-2][1]:
        print('?')
    else:
        print(items[-1][0].upper())
