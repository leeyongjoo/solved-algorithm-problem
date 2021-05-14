# My solution
def my_solution(N, M, weights):
    result = 0
    weights = sorted(weights)
    for i in range(len(weights)):
        for j in range(i+1, len(weights)):
            if weights[i] != weights[j]:
                result += 1
    return result

# Book's solution
def solution(N, M, weights):
    balls = [0] * (M + 1) # index는 공의 무게
    for w in weights:
        balls[w] += 1

    result = 0
    n = N
    for i in range(len(balls)):
        n -= balls[i]  # balls[i]: 같은 무게의 공의 개수 (A의 경우의 수) / n: i 무게보다 큰 나머지 공의 개수 (B의 경우의 수)
        result += n * balls[i]
    return result


N, M = 5, 3
weights = [1, 3, 2, 3, 2]
print(my_solution(N, M, weights))
print(solution(N, M, weights))
# 8

N, M = 8, 5
weights = [1, 5, 4, 3, 2, 4, 5, 2]
print(my_solution(N, M, weights))
print(solution(N, M, weights))
# 25
