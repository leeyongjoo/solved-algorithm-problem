# https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3
def solution(numbers, target):
    from collections import deque
    dq = deque([(0, 0)])
    cnt = 0
    while dq:
        nums_sum, idx = dq.popleft()

        if idx == len(numbers):
            if nums_sum == target:
                cnt += 1
        else:
            dq.append((nums_sum + numbers[idx], idx + 1))
            dq.append((nums_sum - numbers[idx], idx + 1))
    return cnt


if __name__ == "__main__":
    print(solution([1, 1, 1, 1, 1], 3))
    print(solution([1, 1, 1, 1, 1], 3) == 5)
