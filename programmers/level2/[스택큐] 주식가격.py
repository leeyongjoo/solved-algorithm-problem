# https://programmers.co.kr/learn/courses/30/lessons/42584?language=python3
def solution(prices):
    ans = [0] * len(prices)
    stack = []
    for i, p in enumerate(prices):
        while stack and prices[stack[-1]] > p:
            idx = stack.pop()
            ans[idx] = i - idx
        else:
            stack.append(i)
    while stack:
        idx = stack.pop()
        ans[idx] = len(prices) - 1 - idx
    return ans


if __name__ == "__main__":
    print(solution([1, 2, 3, 2, 3]))
    print(solution([1, 2, 3, 2, 3]) == [4, 3, 1, 1, 0])
