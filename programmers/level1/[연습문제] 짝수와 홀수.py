# https://programmers.co.kr/learn/courses/30/lessons/12937?language=python3
def solution(num):
    return "Odd" if num % 2 else "Even"


if __name__ == "__main__":
    print(solution(3))
    print(solution(3) == "Odd")
    print(solution(4))
    print(solution(4) == "Even")
