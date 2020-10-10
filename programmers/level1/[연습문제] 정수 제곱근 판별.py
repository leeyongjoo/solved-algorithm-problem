# https://programmers.co.kr/learn/courses/30/lessons/12934?language=python3
def solution(n):
    sqr = n ** 0.5
    if int(sqr) == sqr:
        return int((sqr + 1) ** 2)
    else:
        return -1


if __name__ == "__main__":
    print(solution(121))
    print(solution(121) == 144)
    print(solution(3))
    print(solution(3) == -1)
