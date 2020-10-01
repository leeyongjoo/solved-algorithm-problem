# https://programmers.co.kr/learn/courses/30/lessons/17680?language=python3
from collections import deque


def solution(cacheSize, cities):
    dq = deque(maxlen=cacheSize)
    cnt_time = 0
    for city in cities:
        c = city.lower()
        if c in dq:
            cnt_time += 1
            dq.remove(c)
        else:
            cnt_time += 5
        dq.append(c)
    return cnt_time


if __name__ == "__main__":
    # print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
    # print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]) == 50)
    # print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
    # print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]) == 21)
    # print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
    # print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]) == 60)
    print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju",
                       "NewYork", "Rome"]))
    print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju",
                       "NewYork", "Rome"]) == 52)
    # print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
    # print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]) == 16)
    # print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
    # print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]) == 25)
