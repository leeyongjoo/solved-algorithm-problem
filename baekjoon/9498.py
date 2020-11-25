# 9498: 시험 성적
# https://www.acmicpc.net/problem/9498

a = int(input())
if 90 <= a:
    print('A')
elif 80 <= a:
    print('B')
elif 70 <= a:
    print('C')
elif 60 <= a:
    print('D')
else:
    print('F')