# https://programmers.co.kr/learn/courses/30/lessons/12931?language=python3
def solution(n):
    return sum([int(a) for a in str(n)])


if __name__ == "__main__":
    print(solution(123))
    print(solution(123) == 6)
    print(solution(987))
    print(solution(987) == 24)
