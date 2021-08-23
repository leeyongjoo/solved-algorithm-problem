# 행렬에서 해당하는 번호를 dfs 방식으로 찾아주는 함수
def find_nums_dfs(matrix, to_find_num):
    direction = [
        (0, 1), (1, 0), (0, -1), (-1, 0)  # 동, 남, 서, 북
    ]

    rn = len(matrix)
    cn = len(matrix[0])

    block = []
    blocks = []

    for i in range(rn):
        for j in range(cn):
            if matrix[i][j] == to_find_num:

                stack = [(i, j)]
                while len(stack) > 0:
                    x, y = stack.pop()

                    if 0 <= x < rn and 0 <= y < cn:
                        if matrix[x][y] == to_find_num:
                            matrix[x][y] = -1
                            block.append([x, y])
                            for dx, dy in direction:
                                stack.append((x + dx, y + dy))
                blocks.append(block)
                block = []
    return blocks


# 블럭을 회전시켜주는 함수
def rotate_block(block):
    n = max(map(lambda a: max(a), block))
    new_blocks = []
    for x, y in block:
        new_blocks.append([y, n - x])
    return new_blocks


# 0 좌표로 이동시켜주는 함수
def move_block_to_zero(block):
    min_x = min(map(lambda a: a[0], block))
    min_y = min(map(lambda a: a[1], block))
    return list(map(lambda a: [a[0] - min_x, a[1] - min_y], block))


def solution(game_board, table):
    spaces = find_nums_dfs(game_board, 0)
    blocks = find_nums_dfs(table, 1)

    spaces_moved_sorted = list(map(sorted, map(move_block_to_zero, spaces)))  # 2차원
    blocks_rotated_moved_sorted: list[list[list[int]]] = []  # 3차원
    for block in blocks:
        rotated_blocks = [sorted(move_block_to_zero(block))]
        for _ in range(3):
            block = rotate_block(block)  # 회전
            block = move_block_to_zero(block)  # 0 으로 이동
            block = sorted(block)  # 정렬
            rotated_blocks.append(block)
        blocks_rotated_moved_sorted.append(rotated_blocks)

    match_block_cnt = 0
    matched_space = set()
    matched_block = set()

    for i, space in enumerate(spaces_moved_sorted):
        for j, four_blocks in enumerate(blocks_rotated_moved_sorted):

            if i not in matched_space and j not in matched_block:
                if len(spaces[i]) == len(four_blocks[0]):
                    for fbi in range(4):  # four blocks index
                        if space == four_blocks[fbi]:
                            match_block_cnt += len(four_blocks[fbi])
                            matched_space.add(i)
                            matched_block.add(j)
                            break
    return match_block_cnt


# 49: 빈공간과 블럭을 구한다.
# 52: 빈공간은 회전시켜놓지 않고, 이동과 정렬만 수행해서 리스트에 담는다. -> 2차원
# 53: 블럭은 미리 회전, 이동, 정렬을 수행한 결과(2차원 리스트)를 리스트에 담는다. -> 3차원

# 70: 이미 매치된 블럭 여부 검사
# 71: 블럭의 가중치가 같은 지 검사
# 72: 회전된 블럭들을 검사

if __name__ == "__main__":
    gb, t = [[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0],
             [0, 1, 1, 1, 0, 0]], [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0],
                                   [1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0]]
    # 14
    print(solution(gb, t))

    gb, t = [[0, 0, 0], [1, 1, 0], [1, 1, 1]], [[1, 1, 1], [1, 0, 0], [0, 0, 0]]
    # 0
    print(solution(gb, t))

    gb = [[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0], [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
          [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
          [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0],
          [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0], [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0],
          [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]]
    t = [[1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1],
         [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0], [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
         [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1],
         [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1], [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1],
         [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1], [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]]
    # 54
    print(solution(gb, t))

    # # ========== 테스트용 코드 ==========
    # def print_gb_t(gb, t):
    #     for row1, row2 in zip(gb, t):
    #         for col in row1:
    #             if col == 0:
    #                 print(col, end=' ')
    #             else:
    #                 print(' ', end=' ')
    #         print(end='\t')
    #         for col in row2:
    #             if col == 1:
    #                 print(col, end=' ')
    #             else:
    #                 print(' ', end=' ')
    #         print()
    #
    # def print_block(block):
    #     for row in block:
    #         for col in row:
    #             if col == 1:
    #                 print(col, end=' ')
    #             else:
    #                 print(' ', end=' ')
    #         print()
    #
    # # 1. 빈공간과 블럭을 구한다.
    # spaces = find_nums_dfs(gb, 0)
    # blocks = find_nums_dfs(t, 1)
    #
    # # 2. 0 좌표로 옮긴 후 정렬
    # spaces = list(map(sorted, map(move_block_to_zero, spaces)))
    # blocks = list(map(sorted, map(move_block_to_zero, blocks)))
    #
    # for i, space in enumerate(spaces):
    #     N = max(map(lambda x: max(x), space)) + 1
    #     tmp_space = [[0 for _ in range(N)] for _ in range(N)]
    #
    #     for i, j in space:
    #         tmp_space[i][j] = 1
    #
    #     print(f'{i}번째 space')
    #     print_block(tmp_space)
    #
    #     print(f'회전 결과')
    #     for _ in range(4):
    #         tmp_space = [[0 for _ in range(N)] for _ in range(N)]
    #         space = rotate_block(space)
    #         space = rotate_block(space)
    #
    #         for i, j in space:
    #             tmp_space[i][j] = 1
    #
    #         print(space)
    #         print_block(tmp_space)
    #         print()
    #
    # # print(spaces)
    # # print(blocks)
