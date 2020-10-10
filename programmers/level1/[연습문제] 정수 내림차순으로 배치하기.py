# https://programmers.co.kr/learn/courses/30/lessons/12933?language=python3
def solution(n):
    nums = [a for a in str(n)]
    return int(''.join(sorted(nums, reverse=True)))


if __name__ == "__main__":
    print(solution(118372))
    print(solution(118372) == 873211)
