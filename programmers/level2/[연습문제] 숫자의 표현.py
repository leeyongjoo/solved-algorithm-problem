# https://programmers.co.kr/learn/courses/30/lessons/12924?language=python3
def solution(n):
    cnt = 0
    for i in range(1, n // 2 + 1):
        num = 0
        while num < n:
            num += i
            i += 1
        if num == n:
            cnt += 1
    return cnt + 1


if __name__ == "__main__":
    print(solution(15))
    print(solution(15) == 4)
