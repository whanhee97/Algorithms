# 프로그래머스 탐욕법 - 구명보트
# https://programmers.co.kr/learn/courses/30/lessons/42885


import math
from collections import deque


def solution1(people, limit):
    answer = 0
    people.sort(reverse=True)
    while people:
        person = people.pop()
        for i in range(len(people)):
            if people[i] + person <= limit:
                people.pop(i)
                break
        answer += 1

    return answer


def solution2(people, limit):
    answer = 0
    people.sort(reverse=True)  # 무거운 순으로 정렬
    dq = deque(people)
    while dq:
        first = dq[0]  # 맨앞
        last = dq[-1]  # 맨뒤
        if first + last <= limit and len(dq) >= 2:
            dq.popleft()
            dq.pop()
        else:
            dq.popleft()
        answer += 1

    return answer


def solution3(people, limit):
    answer = 0
    people.sort(reverse=True)  # 무거운 순으로 정렬
    first = 0
    last = len(people)-1
    while first <= last:
        if people[first] <= limit/2:
            answer += math.ceil((last-first + 1)/2)
            break
        answer += 1
        if people[first] + people[last] <= limit:
            first += 1
            last -= 1
        else:
            first += 1

    return answer


print(solution2([70, 50, 80, 50], 100))
