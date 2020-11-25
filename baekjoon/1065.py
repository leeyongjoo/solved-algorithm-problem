# 1065: 한수
# https://www.acmicpc.net/problem/1065

n = int(input())


def is_hansu(x):
    if x < 100:
        return True
    nums = list(map(int, str(x)))
    diff = nums[0] - nums[1]
    for a, b in zip(nums[1:-1], nums[2:]):
        if a - b != diff:
            return False
    return True


hansu_cnt = 0
for i in range(1, n+1):
    if is_hansu(i):
        hansu_cnt += 1
print(hansu_cnt)
