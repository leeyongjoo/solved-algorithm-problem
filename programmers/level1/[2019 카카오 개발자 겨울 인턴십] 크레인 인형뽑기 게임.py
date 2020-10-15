# https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3
def solution(board, moves):
    dolls = []
    for i in range(len(board)):
        row = []
        for j in range(len(board)):
            if board[j][i] != 0:
                row.append(board[j][i])
        dolls.append(row[::-1])

    stack = []
    match_cnt = 0
    for m in moves:
        idx = m - 1
        if dolls[idx]:
            popped_doll = dolls[idx].pop()
            if stack and stack[-1] == popped_doll:
                stack.pop()
                match_cnt += 1
            else:
                stack.append(popped_doll)
    return match_cnt * 2


if __name__ == "__main__":
    print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
                   [1, 5, 3, 5, 1, 2, 1, 4]))
    print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
                   [1, 5, 3, 5, 1, 2, 1, 4]) == 4)
