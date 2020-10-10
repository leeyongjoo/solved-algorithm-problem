# https://programmers.co.kr/learn/courses/30/lessons/12954?language=python3
def solution(x, n):
    return [x + x * i for i in range(n)]


if __name__ == "__main__":
    print(solution(2, 5))
    print(solution(2, 5) == [2, 4, 6, 8, 10])
    print(solution(4, 3))
    print(solution(4, 3) == [4, 8, 12])
    print(solution(-4, 2))
    print(solution(-4, 2) == [-4, -8])
