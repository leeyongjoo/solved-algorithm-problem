# https://programmers.co.kr/learn/courses/30/lessons/12953?language=python3
def solution(arr):
    gcd = 0
    for i in range(min(arr), 0, -1):
        for a in arr:
            if a % i != 0:
                break
        else:
            gcd = i
        if gcd > 0:
            break

    max_cm = 1
    for a in arr:
        max_cm *= a

    for i in range(1 * gcd, max_cm + 1, gcd):
        for a in arr:
            if i % a != 0:
                break
        else:
            return i


if __name__ == "__main__":
    print(solution([2, 6, 8, 14]))
    print(solution([2, 6, 8, 14]) == 168)
    print(solution([1, 2, 3]))
    print(solution([1, 2, 3]) == 6)
