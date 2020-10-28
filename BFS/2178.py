# 백준 2178 - 미로 탐색
import sys
import queue
#input = sys.stdin.readline 뒤에 \n 붙어 버림
n,m = map(int, input().split())
Map = [list(map(int,input())) for _ in range(n)] # 행렬 그래프 입력받기
depth = [[1]*m for _ in range(n)]

def bfs(x,y) :
    q = queue.Queue()
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    q.put((x,y))
    Map[x][y] = -1
    while q.qsize()>0:
        tx,ty = q.get()
        for i in range(4):
            XX = tx+dx[i]
            YY = ty+dy[i]
            if XX < 0 or YY < 0 or XX>=n or YY >=m:
                continue
            if Map[XX][YY] == 1:
                q.put((XX,YY))
                Map[XX][YY] = -1
                depth[XX][YY] = depth[tx][ty] + 1

bfs(0,0)

print(depth[n-1][m-1])
