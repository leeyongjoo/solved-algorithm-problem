# 2577: 숫자의 개수
# https://www.acmicpc.net/problem/2577

mul = 1
for _ in range(3):
    mul *= int(input())
s = str(mul)

digit_cnt = [0] * 10
for a in s:
    digit_cnt[int(a)] += 1
    
for a in digit_cnt:
    print(a)
