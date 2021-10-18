# 백준 - 바이러스
# https://www.acmicpc.net/problem/2606

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

computers = int(input())
n = int(input())

graph = [[] for _ in range(computers+1)]
for _ in range(n):
    frm, to = map(int, input().split())
    graph[frm].append(to)
    graph[to].append(frm)

visited = [0]*(computers+1)


def dfs(here):
    visited[here] = 1
    for i in graph[here]:
        if visited[i] == 0:
            dfs(i)


dfs(1)
print(sum(visited)-1)
