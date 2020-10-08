import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())
Map = [[0 for _ in range(n)]for _ in range(n)]
for i in range(n):
    line = input()
    for j in range(n):
        Map[i][j] = int(line[j])

danjiList = [] #단지 리스트
cnt = 0 # 단지내 아파트 수

def dfs(x,y):
    global n, Map, cnt
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    Map[x][y] = -1 # 아파트 있고 방문했으면 -1로 표시
    cnt += 1 # 방문했으면 cnt에 1추가(아파트 수 적재)
    for i in range(4): # 4방향 탐색
        xx = x + dx[i]
        yy = y + dy[i]
        if xx < 0 or yy < 0 or xx >= n or yy >= n :
            continue
        if Map[xx][yy] == 1: # 아파트가 있으면 
            dfs(xx,yy) # 방문

for i in range(n):
    for j in range(n):
        if Map[i][j] == 1:
            dfs(i,j)
            danjiList.append(cnt)
            cnt = 0

danjiList.sort()
print(len(danjiList))
for a in danjiList:
    print(a)
# for i in range(n):
#     print(Map[i])