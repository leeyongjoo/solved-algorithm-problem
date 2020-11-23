# https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3
def solution(s):
    ans = len(s)
    for i in range(len(s) // 2, 0, -1):
        sliced_s = [s[idx:idx + i] for idx in range(0, len(s), i)] + ['']

        compare_s = sliced_s[0]
        compare_cnt = 1
        compressed = []
        for j in range(1, len(sliced_s)):
            if sliced_s[j] == compare_s:
                compare_cnt += 1
            else:
                compressed.append(f'{compare_cnt}{compare_s}' if compare_cnt > 1 else compare_s)
                compare_s = sliced_s[j]
                compare_cnt = 1
        ans = min(ans, len(''.join(compressed)))
    return ans


if __name__ == "__main__":
    print(solution("aabbaccc"))
    print(solution("aabbaccc") == 7)
    print(solution("ababcdcdababcdcd"))
    print(solution("ababcdcdababcdcd") == 9)
    print(solution("abcabcdede"))
    print(solution("abcabcdede") == 8)
    print(solution("abcabcabcabcdededededede"))
    print(solution("abcabcabcabcdededededede") == 14)
    print(solution("xababcdcdababcdcd"))
    print(solution("xababcdcdababcdcd") == 17)
