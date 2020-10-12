# https://programmers.co.kr/learn/courses/30/lessons/12943?language=python3
def solution(num):
    cnt = 0
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
        cnt += 1

        if cnt == 500:
            return -1
    return cnt


if __name__ == "__main__":
    print(solution(6))
    print(solution(6) == 8)
    print(solution(16))
    print(solution(16) == 4)
    print(solution(626331))
    print(solution(626331) == -1)
    print(solution(1))