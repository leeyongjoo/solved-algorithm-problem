# 8437: Julka
# https://www.acmicpc.net/problem/8437

sum_kn, diff_kn = (int(input()) for _ in range(2))
k = (sum_kn + diff_kn) // 2
print(k)
print(sum_kn - k)