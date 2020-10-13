# https://programmers.co.kr/learn/courses/30/lessons/17682?language=python3
def solution(dartResult):
    bonus_option = ['S', 'D', 'T', '*', '#']
    chrs = [a for a in dartResult if a in bonus_option]

    dr = dartResult
    for bo in bonus_option:
        dr = dr.replace(bo, ' ')
    scores = [int(a) for a in dr.split()]

    i = -1
    for c in chrs:
        if c.isalpha():
            i += 1
            if c == 'D':
                scores[i] **= 2
            elif c == 'T':
                scores[i] **= 3
        elif c == '*':
            scores[i] *= 2
            if i > 0:
                scores[i-1] *= 2
        elif c == '#':
            scores[i] *= -1
    return sum(scores)

if __name__ == "__main__":
    print(solution('1S2D*3T'))
    print(solution('1S2D*3T') == 37)
    print(solution('1D2S#10S'))
    print(solution('1D2S#10S') == 9)
    print(solution('1D2S0T'))
    print(solution('1D2S0T') == 3)
    print(solution('1S*2T*3S'))
    print(solution('1S*2T*3S') == 23)
    print(solution('1D#2S*3S'))
    print(solution('1D#2S*3S') == 5)
    print(solution('1T2D3D#'))
    print(solution('1T2D3D#') == -4)
    print(solution('1D2S3T*'))
    print(solution('1D2S3T*') == 59)
