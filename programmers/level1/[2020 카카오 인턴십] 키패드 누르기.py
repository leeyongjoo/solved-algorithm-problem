# https://programmers.co.kr/learn/courses/30/lessons/67256?language=python3
def solution(numbers, hand):
    left_hand, right_hand = (3, 0), (3, 2)

    result = []
    for num in numbers:
        i, j = (num-1) // 3, (num-1) % 3

        if num in [1, 4, 7]:
            c = 'L'
        elif num in [3, 6, 9]:
            c = 'R'
        else:
            if num == 0:
                i, j = 3, 1

            left_dist = abs(left_hand[0] - i) + abs(left_hand[1] - j)
            right_dist = abs(right_hand[0] - i) + abs(right_hand[1] - j)

            if left_dist < right_dist:
                c = 'L'
            elif right_dist < left_dist:
                c = 'R'
            else:
                if hand.lower() == 'left':
                    c = 'L'
                else:
                    c = 'R'

        result.append(c)
        if c == 'L':
            left_hand = i, j
        elif c == 'R':
            right_hand = i, j

    return ''.join(result)


if __name__ == "__main__":
    print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
    print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right") == "LRLLLRLLRRL")
    print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
    print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left") == "LRLLRRLLLRR")
    print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))
    print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right") == "LLRLLRLLRL")
