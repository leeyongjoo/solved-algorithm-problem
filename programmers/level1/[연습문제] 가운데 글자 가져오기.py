# https://programmers.co.kr/learn/courses/30/lessons/12903?language=python3
def solution(s):
    n = len(s)
    return s[(n - 1) // 2:n // 2 + 1]


if __name__ == "__main__":
    print(solution("abcde"))
    print(solution("abcde") == "c")
    print(solution("qwer"))
    print(solution("qwer") == "we")
