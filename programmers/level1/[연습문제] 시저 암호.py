# https://programmers.co.kr/learn/courses/30/lessons/12926?language=python3
def solution(s, n):
    from string import ascii_lowercase as low
    from string import ascii_uppercase as upp
    result = []
    for c in s:
        if c in low:
            result.append(low[(low.index(c) + n) % len(low)])
        elif c in upp:
            result.append(upp[(upp.index(c) + n) % len(upp)])
        else:
            result.append(c)
    return ''.join(result)


if __name__ == "__main__":
    print(solution("AB", 1))
    print(solution("AB", 1) == "BC")
    print(solution("z", 1))
    print(solution("z", 1) == "a")
    print(solution("a B z", 4))
    print(solution("a B z", 4) == "e F d")
