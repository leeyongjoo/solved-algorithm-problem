# https://programmers.co.kr/learn/courses/30/lessons/12930?language=python3
def solution(s):
    ans = []
    for word in s.split(' '):
        after = []
        for i in range(len(word)):
            if i % 2 == 0:
                after.append(word[i].upper())
            else:
                after.append(word[i].lower())
        ans.append(''.join(after))
    return ' '.join(ans)


if __name__ == "__main__":
    print(solution("try hello world"))
    print(solution("try hello world") == "TrY HeLlO WoRlD")
