# https://programmers.co.kr/learn/courses/30/lessons/12922?language=python3
def solution(n):
    word = "수박"
    words = word * (n // len(word) + 1)
    return words[:n]


if __name__ == "__main__":
    print(solution(3))
    print(solution(3) == "수박수")
    print(solution(4))
    print(solution(4) == "수박수박")
