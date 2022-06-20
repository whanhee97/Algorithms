# 프로그래머스 - 모음사전
# https://programmers.co.kr/learn/courses/30/lessons/84512

from itertools import product


def solution(word):
    answer = 0
    result = []
    for i in range(1, 6):
        for pd in list(product(['A', 'E', 'I', 'O', 'U'], repeat=i)):
            result.append(''.join(pd))

    result.sort()
    return result.index(word) + 1


print(solution("AAA"))
