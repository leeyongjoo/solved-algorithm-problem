# 1439: 뒤집기
# https://www.acmicpc.net/problem/1439

S = "0001100"
# S = input()

result = 0
cnt = [0, 0]  # 각 숫자를 뒤집어야 하는 횟수

prev = S[0]
cnt[int(prev)] = 1
for s in S[1:]:
    if prev != s:
        if s == '0':
            cnt[0] += 1
        else:
            cnt[1] += 1
    prev = s

result = min(cnt)
print(result)
