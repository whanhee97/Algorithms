# 프로그래머스 그래프 - 순위
# https://programmers.co.kr/learn/courses/30/lessons/49191

from collections import Counter


def solution(n, results):
    # p1이 p2에 이겼을 때는 1로,
    # p1이 p2에 졌을 때는 -1로 초기화
    board = [[0] * n for _ in range(n)]
    for p1, p2 in results:
        board[p1 - 1][p2 - 1] = 1
        board[p2 - 1][p1 - 1] = -1

    for k in range(n):                  # 1. 모든 노드를 중간점(경로)로 가정하며
        for i in range(n):              # 2. 점수판을 순회
            for j in range(n):          # 3. 만약 i가 k에 이겼고, k가 j에 이겼다면
                if board[i][j] == 0:    # i는 j에게도 이김 (지는 것도 동일)
                    if board[i][k] == 1 and board[k][j] == 1:
                        board[i][j] = 1
                    elif board[i][k] == -1 and board[k][j] == -1:
                        board[i][j] = -1

    # 각 노드 점수판에 0이 하나(다른 노드들에 대해 승패가 모두 결정됨)인 경우만 셈
    ans = 0
    for i in range(n):
        if Counter(board[i])[0] == 1:
            ans += 1

    return ans


solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])
