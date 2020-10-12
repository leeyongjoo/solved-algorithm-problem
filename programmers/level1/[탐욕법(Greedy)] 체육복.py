# https://programmers.co.kr/learn/courses/30/lessons/42862?language=python3
def solution(n, lost, reserve):
    stolen = sorted(filter(lambda x: x not in reserve, lost))
    lendable = sorted(filter(lambda x: x not in lost, reserve))
    for i in lendable:
        if i - 1 in stolen:
            stolen.remove(i - 1)
        elif i + 1 in stolen:
            stolen.remove(i + 1)
    return n - len(stolen)


if __name__ == "__main__":
    print(solution(5, [2, 4], [1, 3, 5]))
    print(solution(5, [2, 4], [1, 3, 5]) == 5)
    print(solution(5, [2, 4], [3]))
    print(solution(5, [2, 4], [3]) == 4)
    print(solution(3, [3], [1]))
    print(solution(3, [3], [1]) == 2)
    print(solution(3, [1], [1]))
