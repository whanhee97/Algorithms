# 백준 - n-queen
# https://www.acmicpc.net/problem/9663
# 백트래킹 문제

def is_promising(cdx):
    for i in range(cdx):  # cdx행 전까지 체크
        # cdx행과 그전의 행들을 비교해서 열이 같으면 위아래로 같은 것이고 행끼리 뺀값이 열끼리 뺀값이랑 같으면 대각선으로 같음
        if board[cdx] == board[i] or abs(board[cdx]-board[i]) == cdx-i:
            return False
    return True


def n_queen(cdx):
    global cnt
    if cdx == n:  # 행이 n끝까지 왔으면 가능한것 이므로 경우의 수 + 1
        cnt += 1
        return
    for i in range(n):  # i는 열
        board[cdx] = i  # 해당 행의 i번째 열에 퀸을 놓아 봄
        if is_promising(cdx):  # 유망한지 체크
            n_queen(cdx + 1)  # 유망 하면 다음 행도 확인


n = int(input())
cnt = 0
board = [-1]*n
n_queen(0)
print(cnt)
