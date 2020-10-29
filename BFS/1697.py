# 백준 1697 - 숨바꼭질
import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int, input().split())

def bfs(n,k):
    q = deque()
    q.append(n)
    visited = [0]*100001
    visited[n] = 1
    dx = [-1, 1]
    while q:
        tx = q.popleft() # 큐에꺼 하나 빼서
        if tx == k: # k랑 같으면 종료
            return visited[tx]-1
        
        for i in range(3): # 3가지 비교 (앞으로 걷기, 뒤로 걷기, 순간 이동)
            if i == 2:
                xx = 2*tx # 순간이동
            else:
                xx = tx + dx[i] # 걷기

            if xx < 0 or xx >= 100001: # 범위 밖으로 가면 넘어감
                continue
            if visited[xx] == 0: # 방문 안했으면 
                visited[xx] = visited[tx]+1 # depth를 이전꺼에서 1 올려주고 
                q.append(xx) # 큐에 추가

            
print(bfs(n,k))
