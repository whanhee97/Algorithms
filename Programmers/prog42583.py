# 프로그래머스 스택/큐 - 다리를 지나는 트럭
# https://programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque


def shift_left(bridge):
    for i in range(1, len(bridge)):
        bridge[i-1] = bridge[i]

    bridge[-1] = 0


def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    bridge = [0]*bridge_length
    while truck_weights:
        shift_left(bridge)
        answer += 1
        if sum(bridge) + truck_weights[0] <= weight:
            bridge[-1] = truck_weights.popleft()
    while 1:
        if sum(bridge) != 0:
            shift_left(bridge)
            answer += 1
        else:
            break
    return answer


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
