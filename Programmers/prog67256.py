# 프로그래머스 - 키패드 누르기
# https://programmers.co.kr/learn/courses/30/lessons/67256
def get_distance(x1, x2):
    keypad = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
        '*': [3, 0], 0: [3, 1], '#': [3, 2]
    }
    pos_x1 = keypad[x1]
    pos_x2 = keypad[x2]
    return abs(pos_x1[0]-pos_x2[0])+abs(pos_x1[1]-pos_x2[1])


def solution(numbers, hand):
    answer = ''
    cur_l = '*'
    cur_r = '#'
    while numbers:
        push = numbers.pop(0)
        if push == 1 or push == 4 or push == 7:
            cur_l = push
            answer += 'L'
        elif push == 3 or push == 6 or push == 9:
            cur_r = push
            answer += 'R'
        else:  # 2580 일때
            dis_l = get_distance(push, cur_l)
            dis_r = get_distance(push, cur_r)
            if dis_r > dis_l:  # 오른쪽이 더 멀면
                cur_l = push
                answer += 'L'
            elif dis_l > dis_r:  # 왼쪽이 더 멀면
                cur_r = push
                answer += 'R'
            else:  # 둘 거리가 같으면
                if hand == "right":
                    cur_r = push
                    answer += 'R'
                else:
                    cur_l = push
                    answer += 'L'
    return answer


solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
