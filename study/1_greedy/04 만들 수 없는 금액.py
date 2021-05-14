N, coins = 5, [3, 2, 1, 1, 9]


# My solution
def my_solution():
    from itertools import combinations
    num_set = set()
    for i in range(1, len(coins) + 1):
        num_set = num_set.union(map(sum, combinations(coins, i)))

    for i, p in enumerate(sorted(list(num_set)), start=1):
        if i != p:
            result = i
            break
    return result


# Book's solution
def solution():
    target = 1  # 0까지는 만들 수 있고, 1을 만들 수 있는 지 판단
    for a in sorted(coins):
        if a > target:  # a <= target 이면 target + a - 1 까지 만들 수 있다는 뜻!
            break
        target += a
    return target


print(my_solution())
print(solution())
# 8
