# 5554: 심부름 가는 길
# https://www.acmicpc.net/problem/5554

time = sum(int(input()) for _ in range(4))
div, mod = divmod(time, 60)
print(div)
print(mod)