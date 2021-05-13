# 프로그래머스 스택/큐 - 프린터
# https://programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque


def solution(priorities, location):
    printed = []
    waitingQue = deque()
    for loc, p in enumerate(priorities):
        waitingQue.append((loc, p))

    while waitingQue:
        Max = max(map(lambda x: x[1], waitingQue))
        temp = waitingQue.popleft()
        if temp[1] >= Max:
            printed.append(temp)
        else:
            waitingQue.append(temp)

    arr = list(map(lambda x: x[0], printed))
    answer = arr.index(location)
    return answer+1


priorities = [2, 1, 3, 2]
location = 2
print(solution(priorities, location))
