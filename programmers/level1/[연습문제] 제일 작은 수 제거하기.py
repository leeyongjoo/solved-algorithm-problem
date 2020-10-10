# https://programmers.co.kr/learn/courses/30/lessons/12935?language=python3
def solution(arr):
    num_min = min(arr)
    arr.remove(num_min)
    return arr or [-1]


if __name__ == "__main__":
    print(solution([4,3,2,1]))
    print(solution([4,3,2,1]) == [4,3,2])
    print(solution([10]))
    print(solution([10]) == [-1])
