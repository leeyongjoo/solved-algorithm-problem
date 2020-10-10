# https://programmers.co.kr/learn/courses/30/lessons/12919?language=python3
def solution(seoul):
    return f'김서방은 {seoul.index("Kim")}에 있다'


if __name__ == "__main__":
    print(solution(["Jane", "Kim"]))
    print(solution(["Jane", "Kim"]) == "김서방은 1에 있다")
