# https://programmers.co.kr/learn/courses/30/lessons/12982?language=python3
def solution(d, budget):
    cnt = 0
    for a in sorted(d):
        budget -= a
        if budget < 0:
            break
        cnt += 1
    return cnt


if __name__ == "__main__":
    print(solution([1,3,2,5,4], 9))
    print(solution([1,3,2,5,4], 9) == 3)
    print(solution([2,2,3,3], 10))
    print(solution([2,2,3,3], 10) == 4)
