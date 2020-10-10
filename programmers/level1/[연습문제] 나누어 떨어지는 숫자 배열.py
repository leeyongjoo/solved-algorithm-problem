# https://programmers.co.kr/learn/courses/30/lessons/12910?language=python3
def solution(arr, divisor):
    ans = [a for a in arr if a % divisor == 0]
    return sorted(ans) if ans else [-1]


if __name__ == "__main__":
    print(solution([5, 9, 7, 10], 5))
    print(solution([5, 9, 7, 10], 5) == [5, 10])
    print(solution([2, 36, 1, 3], 1))
    print(solution([2, 36, 1, 3], 1) == [1, 2, 3, 36])
    print(solution([3, 2, 6], 10))
    print(solution([3, 2, 6], 10) == [-1])
