# My solution
def my_solution(S):
    result = 0
    for s in S:
        num = int(s)
        if num < 2 or result < 2:
            result += num
        else:
            result *= num
    return result


# Book's solution
def solution(S):
    result = int(S[0])
    for i in range(1, len(S)):
        num = int(S[i])
        if num <= 1 or result <= 1:
            result += num
        else:
            result *= num
    return result


S = "02984"
print(my_solution(S))
print(solution(S))
# 576

S = "567"
print(my_solution(S))
print(solution(S))
# 210
