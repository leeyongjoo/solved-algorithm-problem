# https://programmers.co.kr/learn/courses/30/lessons/17681?language=python3
def solution(n, arr1, arr2):
    a1 = [f'{bin(a)[2:]:0>{n}}' for a in arr1]
    a2 = [f'{bin(a)[2:]:0>{n}}' for a in arr2]
    result = []
    for a, b in zip(a1, a2):
        row = []
        for i in range(n):
            if a[i] == '1' or b[i] == '1':
                row.append('#')
            else:
                row.append(' ')
        result.append(''.join(row))
    return result


if __name__ == "__main__":
    print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
    print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10])
          == ["######", "###  #", "##  ##", " #### ", " #####", "### # "])
