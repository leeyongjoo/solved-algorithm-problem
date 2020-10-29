# https://programmers.co.kr/learn/courses/30/lessons/12911?language=python3
def solution(n):
    result = n
    while True:
        result += 1
        if bin(n).count('1') == bin(result).count('1'):
            break
    return result


if __name__ == "__main__":
    print(solution(78))
    print(solution(78) == 83)
    print(solution(15))
    print(solution(15) == 23)
