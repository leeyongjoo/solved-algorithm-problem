# https://programmers.co.kr/learn/courses/30/lessons/12944?language=python3
def solution(arr):
    return sum(arr)/len(arr)


if __name__ == "__main__":
    print(solution([1,2,3,4]))
    print(solution([1,2,3,4]) == 2.5)
    print(solution([5,5]))
    print(solution([5,5]) == 5)
