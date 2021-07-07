# 프로그래머스 Summer/Winter Coding(~2018) - 배달
# https://programmers.co.kr/learn/courses/30/lessons/12978

from collections import deque
import math


def solution(N, road, K):
    answer = 0
    # 맵 그래프 그리기
    maps = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for frm, to, w in road:
        if maps[frm][to] == 0:
            maps[frm][to], maps[to][frm] = w, w
        else:
            if maps[frm][to] > w:
                maps[frm][to], maps[to][frm] = w, w
    
    # 최소거리를 math.inf를 사용해 초기화
    shortestDistances = [math.inf for _ in range(N+1)]
    bfs(1, maps, shortestDistances)
    
    # 최소거리들중 K보다 작은것만 카운트
    for x in shortestDistances:
        if x <= K:
            answer += 1
    return answer


def bfs(start, maps, shortestDistances):
    que = deque()
    que.append(start)
    shortestDistances[start] = 0  # 첫 번째 까지의 최소 거리는 0
    while que:
        cur = que.popleft()
        for i in range(1, len(shortestDistances)):  # i는 1부터 N까지 쭉 둘러봐서
            if maps[cur][i] != 0:  # 0이 아니면 갈 수 있는 곳 -> i
                # 갈 수 있는 곳 까지의 최소거리가 (현재꺼의 최소거리 + 가중치) 보다 크면 업데이트하고 큐에다가 집어넣음
                if shortestDistances[i] > shortestDistances[cur] + maps[cur][i]:
                    shortestDistances[i] = shortestDistances[cur] + maps[cur][i]
                    que.append(i)