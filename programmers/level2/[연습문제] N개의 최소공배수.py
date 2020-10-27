# https://programmers.co.kr/learn/courses/30/lessons/12953?language=python3
def compute_gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def compute_lcm(x, y):
    return x * y // compute_gcd(x, y)


def solution(arr):
    lcm = arr[0]
    for a in arr[1:]:
        lcm = compute_lcm(lcm, a)
    return lcm

if __name__ == "__main__":
    print(solution([2, 6, 8, 14]))
    print(solution([2, 6, 8, 14]) == 168)
    print(solution([1, 2, 3]))
    print(solution([1, 2, 3]) == 6)
