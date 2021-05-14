# https://programmers.co.kr/learn/courses/30/lessons/42891?language=python3
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    stack = sorted([(i, ft) for i, ft in enumerate(food_times, start=1)], key=lambda x: x[1], reverse=True)

    cnt_time = 0
    while len(stack) > 0:
        time = stack[-1][1]
        total_time = (time - cnt_time) * len(stack)

        if k >= total_time:
            k -= total_time
            cnt_time += time - cnt_time
            stack.pop()
        else:
            break
    num_list = sorted([i for i, ft in stack])
    return num_list[k % len(num_list)]


if __name__ == "__main__":
    print(solution([3, 1, 2], 5))
    print(solution([3, 1, 2], 5) == 1)
    print(solution([8, 6, 4], 15))
    print(solution([8, 6, 4], 15) == 2)
