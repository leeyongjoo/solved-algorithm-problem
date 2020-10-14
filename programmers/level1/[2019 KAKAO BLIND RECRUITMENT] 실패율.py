# https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3
def solution(N, stages):
    not_clear_and_staged = [[i + 1, 0, 0] for i in range(N)]  # number, not_clear_player staged_player
    for stg in sorted(stages):
        idx = stg - 1
        if idx < N:
            not_clear_and_staged[idx][1] += 1

    staged_player = len(stages)
    for i, lst in enumerate(not_clear_and_staged):
        not_clear_and_staged[i][2] = staged_player
        staged_player -= lst[1]

    result = sorted(not_clear_and_staged, key=lambda x: (x[1] / x[2]) if x[2] > 0 else 0, reverse=True)
    return [lst[0] for lst in result]


if __name__ == "__main__":
    print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
    print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]) == [3, 4, 2, 1, 5])
    print(solution(4, [4, 4, 4, 4, 4]))
    print(solution(4, [4, 4, 4, 4, 4]) == [4, 1, 2, 3])
