# 프로그래머스 그래프 - 가장 먼 노드
# https://programmers.co.kr/learn/courses/30/lessons/49189
from collections import deque

# 인접 행렬로 푼 코드 -> 시간 초과


def solution2(n, edge):
    answer = 0
    g = [[0 for _ in range(n+1)]for _ in range(n+1)]
    visited = [0]*(n+1)
    for e in edge:
        g[e[0]][e[1]] = 1
        g[e[1]][e[0]] = 1

    q = deque()
    layer = 1
    q.append((1, layer))
    visited[1] = 1
    history = []
    while q:
        now, n_layer = q.popleft()
        history.append((now, n_layer))
        for i in range(len(g[now])):
            if g[now][i] == 1 and visited[i] == 0:
                visited[i] = 1
                q.append((i, n_layer+1))

    history.sort(key=lambda x: x[1], reverse=True)
    maxEdge = history[0][1]
    for h in history:
        if h[1] == maxEdge:
            answer += 1
        else:
            break
    return answer


# 인접 리스트로 푼 코드
def solution(n, edge):
    answer = 0
    visited = [0]*(n+1)
    arr = [[]for _ in range(n+1)]  # 인접리스트
    for e in edge:
        arr[e[0]].append(e[1])
        arr[e[1]].append(e[0])
    q = deque()
    layer = 1
    q.append((1, layer))
    visited[1] = 1
    history = []
    while q:
        now, n_layer = q.popleft()
        history.append((now, n_layer))
        for i in arr[now]:
            if visited[i] == 0:
                visited[i] = 1
                q.append((i, n_layer+1))

    history.sort(key=lambda x: x[1], reverse=True)
    maxEdge = history[0][1]
    for h in history:
        if h[1] == maxEdge:
            answer += 1
        else:
            break
    return answer


n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
solution(n, vertex)
