# https://programmers.co.kr/learn/courses/30/lessons/12916?language=python3
def solution(s):
    s_lower = s.lower()
    return s_lower.count('p') == s_lower.count('y')


if __name__ == "__main__":
    print(solution("pPoooyY"))
    print(solution("pPoooyY") == True)
    print(solution("Pyy"))
    print(solution("Pyy") == False)
