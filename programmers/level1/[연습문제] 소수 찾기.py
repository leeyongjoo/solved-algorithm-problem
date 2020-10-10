# https://programmers.co.kr/learn/courses/30/lessons/12921?language=python3
def solution(n):
    # 에라토스테네스의 체
    prime_arr = [False, False] + [True] * (n - 1)
    for i in range(2, n + 1):
        if prime_arr[i] is True:
            for j in range(i * 2, n + 1, i):
                prime_arr[j] = False
    return len([_ for _ in prime_arr if _])


# def solution(n):
#     nums = set(range(2, n + 1))
#     for i in list(nums):
#         if i in nums:
#             nums -= set(range(2 * i, n + 1, i))
#     return len(nums)


if __name__ == "__main__":
    print(solution(10))
    print(solution(10) == 4)
    print(solution(5))
    print(solution(5) == 3)
