# https://programmers.co.kr/learn/courses/30/lessons/68644?language=python3
def solution(numbers):
    numbers_set = set()
    for i, num1 in enumerate(numbers):
        for num2 in numbers[i + 1:]:
            numbers_set.add(num1 + num2)
    return sorted(list(numbers_set))


if __name__ == "__main__":
    print(solution([2, 1, 3, 4, 1]))
    print(solution([2, 1, 3, 4, 1]) == [2, 3, 4, 5, 6, 7])
    print(solution([5, 0, 2, 7]))
    print(solution([5, 0, 2, 7]) == [2, 5, 7, 9, 12])
