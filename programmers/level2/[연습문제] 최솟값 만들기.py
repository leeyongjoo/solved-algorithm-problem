# https://programmers.co.kr/learn/courses/30/lessons/12941?language=python3
def solution(A, B):
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])


if __name__ == "__main__":
    print(solution([1, 4, 2], [5, 4, 4]))
    print(solution([1, 4, 2], [5, 4, 4]) == 29)
    print(solution([1, 2], [3, 4]))
    print(solution([1, 2], [3, 4]) == 10)
