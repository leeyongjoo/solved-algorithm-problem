# https://programmers.co.kr/learn/courses/30/lessons/68935?language=python3
def solution(n):
    three = []
    while n > 0:
        three.append(n % 3)
        n //= 3

    reversed_three = []
    for i, num in enumerate(three[::-1]):
        reversed_three.append(num * (3 ** i))
    return sum(reversed_three)


if __name__ == "__main__":
    print(solution(45))
    print(solution(45) == 7)
    print(solution(125))
    print(solution(125) == 229)
