# 프로그래머스 - 피로도
# https://programmers.co.kr/learn/courses/30/lessons/87946
from itertools import permutations
answer = 0


def dfs(k, dungeons, cnt):
    global answer
    if answer <= cnt:
        answer = cnt
    for i in range(n):
        if visited[i] != 1 and dungeons[i][0] <= k:
            visited[i] = 1
            dfs(k-dungeons[i][1], dungeons, cnt+1)
            visited[i] = 0


def solution(k, dungeons):
    global n, visited
    n = len(dungeons)

    visited = [0]*n

    dfs(k, dungeons, 0)

    return answer


def solution2(k, dungeons):
    answer = -1
    for p_list in permutations(dungeons, len(dungeons)):
        tmp = k
        cnt = 0
        for p in p_list:
            if tmp >= p[0]:
                cnt += 1
                tmp -= p[1]
        answer = max(cnt, answer)
    return answer


k = 80
dungeons = [[80, 10], [50, 40], [70, 50], [30, 10], [50, 30]]

print(solution(k, dungeons))
