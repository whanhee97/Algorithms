# Summer/Winter Coding(~2018) - 예산
# https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    answer = 0
    d.sort()
    for req in d:
        if budget >= req:
            budget -= req
            answer += 1
    return answer
