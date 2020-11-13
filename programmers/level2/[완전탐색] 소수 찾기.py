# https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3
def solution(numbers):
    from itertools import permutations
    nums = set()
    for i in range(1, len(numbers) + 1):
        nums.update([int(''.join(a)) for a in permutations(numbers, i)])

    num_max = max(nums)
    primes = [False, False] + [True] * (num_max - 1)
    for i in range(2, int(num_max ** 0.5) + 1):
        if primes[i]:
            for j in range(i * 2, num_max + 1, i):
                primes[j] = False

    cnt_num_prime = 0
    for n in nums:
        if primes[n]:
            cnt_num_prime += 1
    return cnt_num_prime

    return answer


if __name__ == "__main__":
    print(solution("17"))
    print(solution("17") == 3)
    print(solution("011"))
    print(solution("011") == 2)
