# https://programmers.co.kr/learn/courses/30/lessons/12899?language=python3
def solution(n):
    result = []
    lang = '124'
    while n > 0:
        n -= 1
        result.append(lang[n % len(lang)])
        n //= len(lang)
    return ''.join(result[::-1])


if __name__ == "__main__":
    print(solution(1))
    print(solution(1) == 1)
    print(solution(2))
    print(solution(2) == 2)
    print(solution(3))
    print(solution(3) == 4)
    print(solution(4))
    print(solution(4) == 11)
    print(solution(7))
    print(solution(7) == 21)
