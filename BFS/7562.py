# 백준 7562 - 나이트의 이동
import sys
from collections import deque # ㅡ,.ㅡ 이제 부터 덱 쓰자 queue 쓰니까 백준에서 시간초과 난다
input = sys.stdin.readline
testCase = int(input())

def bfs_night(x,y):
    global toX, toY, Map
    q = deque()
    q.append([x,y])
    dx = [-2,-1,1,2,2,1,-1,-2]
    dy = [1,2,2,1,-1,-2,-2,-1]
    Map[x][y] = 1
    while q:
        tx,ty = q.popleft()
        if tx == toX and ty == toY:
            break
        for i in range(8):
            xx = tx + dx[i]
            yy = ty + dy[i]
            if xx < 0 or yy < 0 or xx >= l or yy >= l:
                continue
            if Map[xx][yy] == 0:
                Map[xx][yy] = 1
                q.append([xx,yy])
                Map[xx][yy] = Map[tx][ty] + 1

for _ in range(testCase):
    l = int(input()) # 체스판 크기 (l * l)
    px,py = map(int,input().split()) # 현재있는 칸
    toX,toY = map(int,input().split()) # 가려는 칸
    Map = [[0]*l for _ in range(l)]
    if px == toX and py == toY:
        print(0)
    else:
        bfs_night(px,py)
        print(Map[toX][toY]-1)

    