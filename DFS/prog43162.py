# 프로그래머스 깊이/너비 우선 탐색(DFS/BFS) - 네트워크
# https://programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    visit = [0] * len(computers)
    answer = 1
    dfs(computers, visit, 0)
    while 1:
        if sum(visit) == len(computers):
            break
        for i in range(len(visit)):
            if visit[i] == 0:
                dfs(computers, visit, i)
                answer += 1
    return answer


def dfs(computers, visit, node):
    visit[node] = 1
    for i in range(len(computers)):
        if computers[node][i] == 1 and node != i:
            if visit[i] == 0:
                dfs(computers, visit, i)


n = 6
computers = [[1, 0, 1, 1, 0, 0], [0, 1, 0, 0, 1, 1], [1, 0, 1, 1, 1, 1], [
    1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1]]
print(solution(n, computers))
