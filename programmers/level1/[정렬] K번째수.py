# https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3
def solution(array, commands):
    ans = []
    for i, j, k in commands:
        new_arr = sorted(array[i - 1:j])
        ans.append(new_arr[k - 1])
    return ans


if __name__ == "__main__":
    print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
    print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]) == [5, 6, 3])
