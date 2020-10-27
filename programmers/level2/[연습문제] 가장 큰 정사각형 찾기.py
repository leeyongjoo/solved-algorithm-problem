# https://programmers.co.kr/learn/courses/30/lessons/12905?language=python3
def solution(board):
    import copy
    dp = copy.deepcopy(board)
    for i in range(1, len(dp)):
        for j in range(1, len(dp[i])):
            if dp[i][j] > 0:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
    n = max([col for row in dp for col in row])
    return n ** 2


if __name__ == "__main__":
    print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))
    print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]) == 9)
    print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))
    print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]) == 4)
