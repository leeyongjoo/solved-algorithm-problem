# https://programmers.co.kr/learn/courses/30/lessons/42587?language=python3
def solution(priorities, location):
    from collections import deque
    dq_priotities = deque([(p, True) if i == location else (p, False) for i, p in enumerate(priorities)])
    dq_sorted_priotities = deque(sorted(priorities, reverse=True))
    time = 0
    while True:
        while dq_priotities[0][0] != dq_sorted_priotities[0]:
            dq_priotities.append(dq_priotities.popleft())

        time += 1
        pri, loc = dq_priotities.popleft()
        dq_sorted_priotities.popleft()

        if loc:
            return time


if __name__ == "__main__":
    print(solution([2, 1, 3, 2], 2))
    print(solution([2, 1, 3, 2], 2) == 1)
    print(solution([1, 1, 9, 1, 1, 1], 0))
    print(solution([1, 1, 9, 1, 1, 1], 0) == 5)
