# https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3
def solution(progresses, speeds):
    from collections import deque
    prs = deque(progresses)
    sps = deque(speeds)
    deploy_cnt = []
    while prs:
        for i in range(len(prs)):
            prs[i] += sps[i]

        cnt = 0
        while prs and prs[0] >= 100:
            prs.popleft()
            sps.popleft()
            cnt += 1

        if cnt > 0:
            deploy_cnt.append(cnt)
    return deploy_cnt


def solution(progresses, speeds):
    from collections import deque
    required_day = deque([(100-p) / s for p, s in zip(progresses, speeds)])
    deploy_cnt = []

    while required_day:
        day = required_day.popleft()
        cnt = 1

        while required_day and required_day[0] < day:
            required_day.popleft()
            cnt += 1
        deploy_cnt.append(cnt)
    return deploy_cnt


if __name__ == "__main__":
    print(solution([93, 30, 55], [1, 30, 5]))
    print(solution([93, 30, 55], [1, 30, 5]) == [2, 1])
    print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
    print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]) == [1, 3, 2])
