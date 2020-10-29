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
    q.put((x,y)) # 맨처음 넣고
    Map[x][y] = -1 # 방문한건 -1 로 표시
    while q.qsize()>0:
        tx,ty = q.get() #첫 번째 빼서
        for i in range(4): # 4방향으로 탐색
            XX = tx+dx[i]
            YY = ty+dy[i]
            if XX < 0 or YY < 0 or XX>=n or YY >=m: # 범위 체크
                continue
            if Map[XX][YY] == 1: # 방문을 아직 안했다면 
                q.put((XX,YY)) # 큐에 넣고
                Map[XX][YY] = -1 # 방문 표시
                depth[XX][YY] = depth[tx][ty] + 1 # BFS의 핵심 간선의 개수 구하기

bfs(0,0)

print(depth[n-1][m-1])
