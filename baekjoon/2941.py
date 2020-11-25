# 2941: 크로아티아 알파벳
# https://www.acmicpc.net/problem/2941

croatia_lang = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt, i = 0, 0
s = input()
while i < len(s):
    word = s[i:i + 2]
    if word == 'dz':
        if i + 2 < len(s) and s[i + 2] == '=':
            i += 2
    elif word in croatia_lang:
        i += 1
    i += 1
    cnt += 1
print(cnt)
