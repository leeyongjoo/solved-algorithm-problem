# https://programmers.co.kr/learn/courses/30/lessons/12945?language=python3
def solution(n):
    fb = [0, 1]
    for _ in range(n - 1):
        fb.append(fb[-2] + fb[-1])
    return fb[n] % 1234567


if __name__ == "__main__":
    print(solution(3))
    print(solution(3) == 2)
    print(solution(5))
    print(solution(5) == 5)
