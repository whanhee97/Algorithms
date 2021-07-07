# 2019 카카오 개발자 겨울 인턴십 / 크레인 인형뽑기 게임
# https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3

import sys
input = sys.stdin.readline

# 내려가서 멈춘곳 반환
def down(board,m):
    for j in range(len(board[0])):
        if board[j][m-1] != 0:
            return j
    return j

#터트리기
def bang(basket):
    if len(basket)>=2:
        if basket[-1] == basket[-2]:
            del basket[-1]
            del basket[-1]
            return True
    return False

def solution(board, moves):
    answer = 0
    basket = []
    for m in moves:
        stop = down(board,m)
        doll = board[stop][m-1]
        board[stop][m-1] = 0
        if doll != 0:
            basket.append(doll)
            if bang(basket):
                answer += 2
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,4,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
board =  [[0,2,0],[1,2,0],[2,2,1]]
moves = [1,2,2,2,1,3]

result = solution(board,moves)

print(result)
