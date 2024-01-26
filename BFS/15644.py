import sys
from collections import deque

queue = deque()
input = sys.stdin.readline

n,m = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(input()))

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx = i
            ry = j
        if board[i][j] == 'B':
            bx = i
            by = j
        if board[i][j] == 'O':
            ox = i
            oy = j

# 0:D, 1:U, 2:L, 3:R
dx = [1,-1,0,0]
dy = [0,0,-1,1]

visit = []
dirDict = {0:'D',1:'U',2:'L',3:'R'}
dirHist = []

def move(x,y,dx,dy):
    cnt = 0
    nx = x
    ny = y
    while board[nx+dx][ny+dy] != '#' and board[nx][ny] != 'O':
        cnt += 1
        nx += dx
        ny += dy

    return (nx,ny,cnt)


queue.append([rx,ry,bx,by,1,[]])
visit.append([rx,ry,bx,by])
def bfs():
    while queue:
        rx,ry,bx,by,depth,dirHist = queue.popleft()
        if depth > 10:
            break

        # 0:D, 1:U, 2:L, 3:R
        for dir in range(4):
            tmpDirHist = dirHist.copy()
            rnx,rny,rcnt = move(rx,ry,dx[dir],dy[dir])
            bnx,bny,bcnt = move(bx,by,dx[dir],dy[dir])
            if bnx == ox and bny == oy:
                continue
            if rnx == ox and rny == oy:
                tmpDirHist.append(dirDict[dir])
                return (depth,tmpDirHist)

            if rnx == bnx and rny == bny:
                if rcnt>bcnt:
                    rnx-=dx[dir]
                    rny-=dy[dir]
                else:
                    bnx-=dx[dir]
                    bny-=dy[dir]
            if [rnx,rny,bnx,bny] not in visit:
                
                tmpDirHist.append(dirDict[dir])
                queue.append([rnx,rny,bnx,bny,depth+1,tmpDirHist])
                visit.append([rnx,rny,bnx,bny])
    return (-1,-1)


result, arr = bfs()


print(result)
if arr != -1:
    print(''.join(arr))

