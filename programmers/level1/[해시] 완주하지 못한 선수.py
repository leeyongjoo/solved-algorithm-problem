# https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3
# 첫 번째로 빠름
def solution(participant, completion):
    from collections import defaultdict
    dd = defaultdict(int)
    for p in participant:
        dd[p] += 1
    for c in completion:
        dd[c] -= 1
    return [k for k, v in dd.items() if v > 0][0]


# # 두 번째
# def solution(participant, completion):
#     part = sorted(participant)
#     comp = sorted(completion)
#     for p, c in zip(part, comp):
#         if p != c:
#             return p
#     return part[-1]
#
#
# # 세 번째
# def solution(participant, completion):
#     from collections import Counter
#     return (Counter(participant) - Counter(completion)).popitem()[0]


if __name__ == "__main__":
    print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
    print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]) == "leo")
    print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
    print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]) == "vinko")
    print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
    print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]) == "mislav")
