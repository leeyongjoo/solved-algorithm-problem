# https://programmers.co.kr/learn/courses/30/lessons/12932?language=python3
def solution(n):
    return [int(a) for a in str(n)[::-1]]


if __name__ == "__main__":
    print(solution(12345))
    print(solution(12345) == [5,4,3,2,1])
