# https://programmers.co.kr/learn/courses/30/lessons/12917?language=python3
def solution(s):
    return ''.join(sorted(s, reverse=True))


if __name__ == "__main__":
    print(solution("Zbcdefg"))
    print(solution("Zbcdefg") == "gfedcbZ")
