# 백준 2644 - 촌수계산
import sys
import queue
input = sys.stdin.readline
n = int(input()) # 사람수
w,z = map(int, input().split()) #구할 관계의 사람 번호
m = int(input()) # 관계수
R = [[0]*(n+1) for _ in range(n+1)] 
visited = [0 for _ in range(n+1)]
q = queue.Queue()
for _ in range(m):
    x,y = map(int,input().split())
    R[x][y] = 1
    R[y][x] = 1

depth =[0 for _ in range(n+1)]

def bfs(w):
    visited[w] = 1
    q.put(w)
    while q.qsize()>0:
        w = q.get()
        for i in range(1,n+1):
            if R[w][i] == 1 and visited[i]==0: # 연결되어있고 방문안했으면 
                q.put(i)
                depth[i] = depth[w] + 1 # 자식 노드에 부모노드 촌수 + 1
                visited[i] = 1
        
bfs(w)
if depth[z] == 0: # 촌수 아무 관계 없으면 -1 출력
    result = -1
else:
    result = depth[z]
print(result)