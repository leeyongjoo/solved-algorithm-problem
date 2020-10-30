# https://programmers.co.kr/learn/courses/30/lessons/12913?language=python3
def solution(land):
    import copy
    dp = copy.deepcopy(land)

    for i in range(len(dp) - 1 - 1, -1, -1):
        for j in range(len(dp[0])):
            dp[i][j] += max(dp[i + 1][:j] + dp[i + 1][j + 1:])
    return max(dp[0])


if __name__ == "__main__":
    print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))
    print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]) == 16)
