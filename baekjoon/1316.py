# 1316: 그룹 단어 체커
# https://www.acmicpc.net/problem/1316

n = int(input())


def is_group_word(word):
    alpha_set = set()
    prev = ''
    for c in word:
        if prev != c:
            if c in alpha_set:
                return False
            else:
                alpha_set.add(c)
        prev = c
    return True


group_word_cnt = 0
for _ in range(n):
    if is_group_word(input()):
        group_word_cnt += 1
print(group_word_cnt)
