# 2480: 주사위 세개
# https://www.acmicpc.net/problem/2480

nums_list = list(map(int, input().split()))
nums_set = set(nums_list)
if len(nums_set) == 1:
    print(10000 + nums_list[0] * 1000)
elif len(nums_set) == 2:
    if nums_list.count(nums_list[0]) > 1:
        print(1000 + nums_list[0] * 100)
    else:
        print(1000 + nums_list[1] * 100)
else:
    print(max(nums_list) * 100)
