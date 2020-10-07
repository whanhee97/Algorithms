# 백준 1012 - 유기농 배추
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000) # 재귀 한계 설정

## 배추가 심어져있고 방문 안한상태이면 1 방문한 상태이면 -1 그외 0

def dfs(x,y):
    global Map, m,n
    Map[x][y] = -1 # 배추가 심어져 있고 방문했으면 -1 표시
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    for i in range(4): # 상,하,좌,우 4방향 다돌음
        if x+dx[i] < m and y+dy[i] < n and x+dx[i] >= 0 and y+dy[i] >= 0 : #경계 넘어서면 패스
            if Map[x+dx[i]][y+dy[i]] == 1 : # 1은 배추가 심어졌는데 방문 안한거
                dfs(x+dx[i],y+dy[i]) # 배추가 심어졌는데 방문 안했으면 방문
t = int(input())

for _ in range(t):
    baechuBug = 0
    m,n,k = map(int,input().split()) # m 행 /  n열 /  k위치
    Map = [[0 for _ in range(n)]for _ in range(m)] # 2차원 배열 0으로 초기화
    for _ in range(k):
        x,y = map(int,input().split())
        Map[x][y] = 1 # 배추가 심어진 곳 1 표시
    for i in range(m):
        for j in range(n): # Map 하나씩 차례로 돌면서
            if Map[i][j] == 1: # 배추가 심어져있고 방문을 안했으면
                dfs(i,j) 
                baechuBug += 1 #배추벌레 한 마리 추가
    print(baechuBug)
