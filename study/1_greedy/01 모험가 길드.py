N, h = 5, [2, 3, 1, 2, 2]

# My solution
def my_solution():
    h.sort()
    result = 0
    i = 0
    while i < N:
        group = h[i:i + h[i]]

        i += max(group)
        if i >= N:
            break

        result += 1
    return result

# Book's solution
def solution():
    h.sort()
    result = 0

    group_cnt = 0
    for i in h:
        group_cnt += 1
        if group_cnt >= i:
            result += 1
            group_cnt = 0

    return result

print(my_solution())  # 2
print(solution())  # 2
