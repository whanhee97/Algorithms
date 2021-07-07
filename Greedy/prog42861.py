# 프로그래머스 탐욕법 - 섬 연결하기
# https://programmers.co.kr/learn/courses/30/lessons/42861

from math import inf


def solution(n, costs):
    answer = 0
    Map = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        Map[i][i] = 0
    for cost in costs:
        Map[cost[0]][cost[1]] = cost[2]
        Map[cost[1]][cost[0]] = cost[2]

    costs_sorted = sorted(costs, key=lambda x: x[2])
    first = costs_sorted.pop(0)
    visited = [0] * n
    visited[first[0]] = 1
    visited[first[1]] = 1
    answer += first[2]
    while 1:
        Min = inf
        Min_idx = 0
        if visited.count(1) == n:
            break
        for i in range(len(Map)):
            if visited[i] == 0:
                continue
            for j in range(len(Map[0])):
                if visited[j] == 1:
                    continue
                if Map[i][j] <= Min and Map[i][j] != 0:
                    Min_idx = j
                    Min = Map[i][j]

        visited[Min_idx] = 1
        answer += Min
    return answer


#print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]), 4)
print(solution(5, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [
      3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]]), 15)

# 5 [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]] 8
# 4 [[0, 1, 5], [1, 2, 3], [2, 3, 3], [1, 3, 2], [0, 3, 4]] 9
# 5 [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]] 104
# 6 [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]] 11
# 5 [[0, 1, 1], [2, 3, 1], [3, 4, 2], [1, 2, 2], [0, 4, 100]] 6
# 5 [[0, 1, 1], [0, 4, 5], [2, 4, 1], [2, 3, 1], [3, 4, 1]] 8
# 5 [[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [1, 3, 1]] 8
