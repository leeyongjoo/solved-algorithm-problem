# https://programmers.co.kr/learn/courses/30/lessons/12907?language=python3
def solution(n, money):
    dp = [[] for _ in range(n + 1)]

    for m in sorted(money):
        dp[m].append([m])

        for i in range(1, len(dp) - m):
            for a in dp[i]:
                dp[i + m].append(a + [m])

        # for i, dp1 in enumerate(dp):
        #     print(i, dp1)
        # print()

    return len(dp[n]) % 1000000007


def solution(n, money):
    dp = [0 for _ in range(n + 1)]

    for m in sorted(money):
        dp[m] += 1

        for i in range(1, len(dp) - m):
            dp[i + m] += dp[i]

    return dp[n] % 1000000007


if __name__ == "__main__":
    print(solution(5, [1, 2, 5]))
    print(solution(5, [1, 2, 5]) == 4)
