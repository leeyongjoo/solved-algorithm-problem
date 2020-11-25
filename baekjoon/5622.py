# 5622: 다이얼
# https://www.acmicpc.net/problem/5622

s = input().lower()
alpha = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
time = 0
for c in s:
    for i, a in enumerate(alpha):
        if c in a:
            time += i + 3
print(time)
