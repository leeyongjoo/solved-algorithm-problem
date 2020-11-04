# https://programmers.co.kr/learn/courses/30/lessons/12939?language=python3
def solution(s):
    nums = [int(a) for a in s.split()]
    return f'{min(nums)} {max(nums)}'


if __name__ == "__main__":
    print(solution("1 2 3 4"))
    print(solution("1 2 3 4") == "1 4")
    print(solution("-1 -2 -3 -4"))
    print(solution("-1 -2 -3 -4") == "-4 -1")
    print(solution("-1 -1"))
    print(solution("-1 -1") == "-1 -1")
