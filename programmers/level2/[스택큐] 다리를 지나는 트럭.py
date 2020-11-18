# https://programmers.co.kr/learn/courses/30/lessons/42583?language=python3
def solution(bridge_length, weight, truck_weights):
    from collections import deque
    truck_q = deque(truck_weights)
    bridge_q = deque()
    bridge_weight = 0

    time = 0
    while truck_q or bridge_q:
        while bridge_q and bridge_q[0][1] == bridge_length:
            bridge_weight -= bridge_q.popleft()[0]

        if truck_q and truck_q[0] + bridge_weight <= weight:
            truck_weight = truck_q.popleft()
            bridge_q.append([truck_weight, 0])
            bridge_weight += truck_weight

        for i in range(len(bridge_q)):
            bridge_q[i][1] += 1
        time += 1
    return time


def solution(bridge_length, weight, truck_weights):
    from collections import deque
    truck_weights = deque(truck_weights)
    bridge_q = deque([0] * bridge_length)
    bridge_w = 0

    time = 0
    while truck_weights or bridge_w > 0:
        bw = bridge_q.popleft()
        if bw > 0:
            bridge_w -= bw

        if truck_weights and bridge_w + truck_weights[0] <= weight:
            tw = truck_weights.popleft()
            bridge_w += tw
            bridge_q.append(tw)
        else:
            bridge_q.append(0)
        time += 1
    return time




if __name__ == "__main__":
    print(solution(2, 10, [7, 4, 5, 6]))
    print(solution(2, 10, [7, 4, 5, 6]) == 8)
    print(solution(100, 100, [10]))
    print(solution(100, 100, [10]) == 101)
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 110)
