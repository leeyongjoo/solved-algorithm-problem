# https://programmers.co.kr/learn/courses/30/lessons/12951?language=python3
def solution(s):
    sep = ' '
    jadencases = []
    for word in s.split(sep):
        if word:
            jadencases.append(word[0].upper() + word[1:].lower())
        else:
            jadencases.append(word)
    return sep.join(jadencases)


if __name__ == "__main__":
    print(solution("3people unFollowed me"))
    print(solution("3people unFollowed me") == "3people Unfollowed Me")
    print(solution("for the last week"))
    print(solution("for the last week") == "For The Last Week")
