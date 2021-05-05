# 프로그래머스 탐욕법(Greedy) - 단속카메라
# https://programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    answer = 1
    sortedRoutes = sorted(routes, key=lambda x: x[0])
    out = sortedRoutes[0][1]
    for r in sortedRoutes[1:]:
        if r[0] > out:
            answer += 1
            out = r[1]
        if out >= r[1]:
            out = r[1]
    return answer


routes = [[-20, 15], [-14, -5], [-18, -13], [-5, -3]]
print(solution(routes))
