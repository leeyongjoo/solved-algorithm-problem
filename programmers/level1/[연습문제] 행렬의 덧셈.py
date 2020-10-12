# https://programmers.co.kr/learn/courses/30/lessons/12950?language=python3
def solution(arr1, arr2):
    ans = []
    for a1, a2 in zip(arr1, arr2):
        row = []
        for i in range(len(a1)):
            row.append(a1[i] + a2[i])
        ans.append(row)
    return ans




if __name__ == "__main__":
    print(solution([[1,2],[2,3]], [[3,4],[5,6]]))
    print(solution([[1,2],[2,3]], [[3,4],[5,6]]) == [[4,6],[7,9]])
    print(solution([[1],[2]], [[3],[4]]))
    print(solution([[1],[2]], [[3],[4]]) == [[4],[6]])
