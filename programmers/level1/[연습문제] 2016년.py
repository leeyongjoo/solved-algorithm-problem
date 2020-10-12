# https://programmers.co.kr/learn/courses/30/lessons/12901?language=python3
def solution(a, b):
    week_string = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    days_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_cnt = b
    for days in days_month[:a - 1]:
        days_cnt += days
    return week_string[days_cnt % len(week_string)]


if __name__ == "__main__":
    print(solution(5, 24))
    print(solution(5, 24) == "TUE")
