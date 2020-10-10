# https://programmers.co.kr/learn/courses/30/lessons/12906?language=python3
def solution(arr):
    result = [arr[0]]
    for a in arr:
        if result[-1] != a:
            result.append(a)
    return result


if __name__ == "__main__":
    print(solution([1, 1, 3, 3, 0, 1, 1]))
    print(solution([1, 1, 3, 3, 0, 1, 1]) == [1, 3, 0, 1])
    print(solution([4, 4, 4, 3, 3]))
    print(solution([4, 4, 4, 3, 3]) == [4, 3])
