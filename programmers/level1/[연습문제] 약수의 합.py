# https://programmers.co.kr/learn/courses/30/lessons/12928?language=python3
def solution(n):
    ans = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            ans.append(i)
    return sum(ans) + n


if __name__ == "__main__":
    print(solution(12))
    print(solution(12) == 28)
    print(solution(5))
    print(solution(5) == 6)
