# 프로그래머스 스택/큐 - 다리를 지나는 트럭
# https://programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    bridge = [0]*bridge_length
    bridge = deque(bridge)
    bridge_weight = 0
    while truck_weights:
        truck_out = bridge.popleft()
        bridge.append(0)
        bridge_weight -= truck_out
        answer += 1
        if bridge_weight + truck_weights[0] <= weight:
            truck_in = truck_weights.popleft()
            bridge[-1] = truck_in
            bridge_weight += truck_in
    while 1:
        if bridge_weight != 0:
            bridge_weight -= bridge.popleft()
            bridge.append(0)
            answer += 1
        else:
            break
    return answer


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
