# https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3
def solution(answers):
    person = [
        (1, 2, 3, 4, 5),
        (2, 1, 2, 3, 2, 4, 2, 5),
        (3, 3, 1, 1, 2, 2, 4, 4, 5, 5),
    ]
    person_correct = [0 for _ in range(len(person))]
    for i, a in enumerate(answers):
        for j in range(len(person)):
            if person[j][i % len(person[j])] == a:
                person_correct[j] += 1
    max_correct = max(person_correct)
    return [i + 1 for i, pc in enumerate(person_correct) if pc == max_correct]


if __name__ == "__main__":
    print(solution([1, 2, 3, 4, 5]))
    print(solution([1, 2, 3, 4, 5]) == [1])
    print(solution([1, 3, 2, 4, 2]))
    print(solution([1, 3, 2, 4, 2]) == [1, 2, 3])
