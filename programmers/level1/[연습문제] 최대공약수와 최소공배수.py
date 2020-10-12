# https://programmers.co.kr/learn/courses/30/lessons/12940?language=python3
def solution(n, m):
    cd = [i for i in range(min(n, m), 0, -1) if n % i == 0 and m % i == 0]
    cm = [j for j in range(1, n * m + 1) if j % n == 0 and j % m == 0]
    return [max(cd), min(cm)]


if __name__ == "__main__":
    print(solution(3, 12))
    print(solution(3, 12) == [3, 12])
    print(solution(2, 5))
    print(solution(2, 5) == [1, 10])
