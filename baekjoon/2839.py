# 2839: 설탕 배달
# https://www.acmicpc.net/problem/2839

N = int(input())
cnt, r = divmod(N, 5)
if r != 0:
    while cnt >= 0:
        cnt_3, r_3 = divmod(N - 5 * cnt, 3)
        if r_3 == 0:
            cnt += cnt_3
            break
        cnt -= 1
print(cnt)
