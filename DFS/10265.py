# 백준 10265 - MT : 못풀었음... 나중에 다시 도전
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
arr = map(int,input().split())
who = [0]
for i in arr:
    who.append(i)

cnt = [0 for _ in range(n+1)]

visited = [False for _ in range(n+1)]
def dfs(v):
    visited[v] = True
    if v != who[v]:
        cnt[who[v]] += 1
    if not visited[who[v]]:
        dfs(who[v])



for j in range(1,n+1):
   
    if visited[j] == False:
        dfs(j)

print(cnt)

