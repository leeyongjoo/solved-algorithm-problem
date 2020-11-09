# https://programmers.co.kr/learn/courses/30/lessons/12949?language=python3
def solution(arr1, arr2):
    matrix = []
    arr2 = list(zip(*arr2))

    for row1 in arr1:
        r = []
        for row2 in arr2:
            num = 0
            for a, b in zip(row1, row2):
                num += a * b
            r.append(num)
        matrix.append(r)
    return matrix


# without zip()
def solution(arr1, arr2):
    matrix = []

    for i in range(len(arr1)):
        r = []
        for j in range(len(arr2[0])):
            num = 0
            for k in range(len(arr1[0])):
                num += arr1[i][k] * arr2[k][j]
            r.append(num)
        matrix.append(r)
    return matrix


if __name__ == "__main__":
    print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
    print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]) == [[15, 15], [15, 15], [15, 15]])
    print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
    print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]) == [[22, 22, 11], [36, 28, 18],
                                                                                             [29, 20, 14]])
