# 프로그래머스 2018 KAKAO BLIND RECRUITMENT - 프렌즈4블록
# https://programmers.co.kr/learn/courses/30/lessons/17679

cnt = 0


def find(m, n, board):  # 스캔하여 찾은 다음 터트린 블럭을 x로 표시하는 함수
    global cnt
    boom = False  # 폭발이 일어나는지 안 일어나는지 판단
    boomSet = set()  # 터진 블럭들의 좌표를 저장함. 겹치는게 있을 수 있으므로 set으로 선언
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] == board[i][j+1] and board[i][j] != 'x':  # 만약에 현재 블럭이 다음 블럭과 같고 x가 아니라면
                if board[i][j] == board[i+1][j]:  # 근데 또 밑에 블럭도 같으면
                    if board[i][j] == board[i+1][j+1]:  # 오른쪽 대각선 밑의 블럭과도 같으면
                        boomSet.add((i, j))  # 4개 블럭 모두 터진블럭 리스트에 추가하자
                        boomSet.add((i+1, j))
                        boomSet.add((i, j+1))
                        boomSet.add((i+1, j+1))
                        boom = True  # 폭탄 터졌다고 체크
    for b in boomSet:  # 터진 블럭들에다가 x표시하고 count 셈
        board[b[0]][b[1]] = 'x'
        cnt += 1
    return boom


def slideDown(m, n, board):  # 중간에 폭탄이 터졌으면 위에 있는 블럭들을 밑으로 내려 주는 함수
    for i in range(m-1, 0, -1):  # 밑에서 부터 순회하면서
        for j in range(n):  # 하나씩 순회하며
            if board[i][j] == 'x':  # 만약에 x이면
                for k in range(i-1, -1, -1):  # 그 위로 쭉 검사해서 x가 아닌것 나타나면 자리를 바꿈
                    if board[k][j] != 'x':
                        temp = board[k][j]
                        board[k][j] = board[i][j]
                        board[i][j] = temp
                        break


def makeBoard(board):  # 입력값을 list로 만들어 주는 함수
    temp = []
    for b in board:
        temp.append(list(b))
    return temp


def solution(m, n, board):
    board = makeBoard(board)  # map으로 만들어 주고
    global cnt
    boom = False
    while 1:
        boom = find(m, n, board)  # 스캔한뒤 터진블럭들 세고 x표시함
        if not boom:  # 터지지 않았다면 루프 빠져나감
            break
        slideDown(m, n, board)  # 밑으로 다 떨궈줌
    return cnt


board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
#board = makeBoard(board)
#find(6, 6, board)
#print(slideDown(6, 6, board))

print(solution(4, 5, board))
