# 프로그래머스 - 9주차_전력망을 둘로 나누기
# https://programmers.co.kr/learn/courses/30/lessons/86971?language=python3
import math


def dfs(here):
    visited[here] = 1
    node = 1
    for i in graph[here]:
        if visited[i] == 0:
            node += dfs(i)
    return node


def solution(n, wires):
    answer = -1
    global graph
    graph = [[] for _ in range(n+1)]
    global visited

    for w in wires:
        graph[w[0]].append(w[1])
        graph[w[1]].append(w[0])
    ans_list = []
    for w in wires:
        visited = [0]*(n+1)
        # 단선
        graph[w[0]].remove(w[1])
        graph[w[1]].remove(w[0])
        # 그룹1 노드 개수
        group1 = dfs(w[0])
        # 그룹2 노드 개수
        group2 = dfs(w[1])
        gap = abs(group1 - group2)
        ans_list.append(gap)

        # 선복구
        graph[w[0]].append(w[1])
        graph[w[1]].append(w[0])

    Min = math.inf
    for a in ans_list:
        if Min >= a:
            Min = a
    return ans_list


solution(9,	[[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]])
