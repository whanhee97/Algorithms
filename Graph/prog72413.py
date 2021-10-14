# 프로그래머스 - 합승 택시 요금
# https://programmers.co.kr/learn/courses/30/lessons/72413
from math import inf


def solution(n, s, a, b, fares):
    answer = 0
    graph = [[inf]*n for _ in range(n)]
    for f in fares:
        graph[f[0]-1][f[1]-1] = f[2]
        graph[f[1]-1][f[0]-1] = f[2]

    for i in range(n):
        graph[i][i] = 0

    # 플로이드 와샬
    for k in range(n):  # 거쳐간 노드
        for i in range(n):  # 출발 노드
            for j in range(n):  # 도착 노드
                if graph[i][k]+graph[k][j] <= graph[i][j]:
                    graph[i][j] = graph[i][k]+graph[k][j]

    # 합승지점 별 최소값 리스트
    c_list = [0]*n

    # 합승 지점이 c일때 (s->c) + (c->a) + (c->b) 최소값 구하기
    for c in range(n):
        c_list[c] = graph[s-1][c] + graph[c][a-1] + graph[c][b-1]

    answer = min(c_list)
    return answer


print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4],
      [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
