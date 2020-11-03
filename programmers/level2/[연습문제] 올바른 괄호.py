# https://programmers.co.kr/learn/courses/30/lessons/12909?language=python3
def solution(s):
    stack = []
    for a in s:
        if a == '(':
            stack.append(a)
        elif a == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
    return len(stack) == 0


if __name__ == "__main__":
    print(solution("()()"))
    print(solution("()()") == True)
    print(solution("(())()"))
    print(solution("(())()") == True)
    print(solution(")()("))
    print(solution(")()(") == False)
    print(solution("(()("))
    print(solution("(()(") == False)
