# 10809: 알파벳 찾기
# https://www.acmicpc.net/problem/10809

from string import ascii_lowercase

s = input()
alpha = ascii_lowercase
alpha_index_list = [-1] * len(alpha)

a_index = ord('a')
for i, c in enumerate(s):
    ail_idx = ord(c) - a_index
    if alpha_index_list[ail_idx] == -1:
        alpha_index_list[ail_idx] = i
print(' '.join(map(str, alpha_index_list)))
