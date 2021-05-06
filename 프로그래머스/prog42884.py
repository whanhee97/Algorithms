# 프로그래머스 탐욕법(Greedy) - 단속카메라
# https://programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    answer = 1  # 1개는 무조건 설치 되어있다고 가정
    sortedRoutes = sorted(routes, key=lambda x: x[0])  # 정렬
    out = sortedRoutes[0][1]  # 첫번째 차의 끝 지점을 out으로 지정
    for r in sortedRoutes[1:]:
        if r[0] > out:  # out보다 현재차의 진입점이 높으면
            answer += 1  # 카메라 설치하고
            out = r[1]  # out 갱신
        if out >= r[1]:  # out보다 현재차의 끝지점이 낮으면 겹치는 것이므로
            out = r[1]  # out 갱신
    return answer


routes = [[-20, 15], [-14, -5], [-18, -13], [-5, -3]]
print(solution(routes))
