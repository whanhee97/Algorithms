# 백준 1742 - 음식물 피하기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

m,n,k = map(int, input().split()) #가로, 세로, 음식물 개수
Map = [[0 for _ in range(n+1)]for _ in range(m+1)] # 전부 0으로 초기화
for _ in range(k): # 음식물 좌표 받고 Map에다 1로 표시
    r,c = map(int,input().split())
    Map[r][c] = 1

trashCan = []
trash=0

def dfs(x,y):
    global n, m, Map, trash
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    Map[x][y] = -1 # 음식물이 있고 방문했으면 -1로 표시
    trash += 1 # 방문했으면 트레쉬에 1추가(크기 적재)
    for i in range(4): # 4방향 탐색
        xx = x + dx[i]
        yy = y + dy[i]
        if xx < 0 or yy < 0 or xx > m or yy > n :
            continue
        if Map[xx][yy] == 1: # 음식물이 있으면 
            dfs(xx,yy) # 방문

for i in range(m+1):
    for j in range(n+1):
        if Map[i][j] == 1: #음식물이 있으면 
            dfs(i,j) #방문하고 
            trashCan.append(trash) #방문끝났으면 연결요소가 끝났기 때문에 음식물 크기 적재한것을 리스트에 저장
            trash = 0 #음식물 크기 초기화

print(max(trashCan))
# for i in range(m+1):
#     print(Map[i])
# print(trashCan)