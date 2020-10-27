# 백준 1260 - DFS와 BFS
import sys
import queue
input = sys.stdin.readline
n,m,v = map(int, input().split())
Map = [[0 for _ in range(n+1)]for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
q = queue.Queue()
for _ in range(m):
    x,y = map(int, input().split())
    Map[x][y] = 1
    Map[y][x] = 1

# dfs는 재귀 이용하거나 스택사용
def dfs(v): 
    visited[v] = 1
    print(v, end = ' ')
    for i in range(1,n+1):
        if Map[v][i] == 1 and visited[i] == 0:
            dfs(i)

#bfs는 큐와 while문 사용
def bfs(v):
    q.put(v) # 큐쓰는 법이 생각안나면 그냥 리스트의 append 이용
    visited[v] = 1
    while q.qsize() > 0 :
        v = q.get() # 큐쓰는 법이 생각안나면 그냥 리스트의 첫번째꺼 가져오고 첫번째 지워주는 del q[0] 이용
        print(v, end = ' ')
        for i in range(1,n+1):
            if Map[v][i] == 1 and visited[i] == 0: # 연결돼있고 방문하지 않았다면
                q.put(i)
                visited[i] = 1 #넣음과 동시에 1로 -> 넣었던걸 또 넣는거 방지
        
dfs(v)
visited = [0 for _ in range(n+1)]
print()
bfs(v)
