#백준 1520 - 내리막 길
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in  range(n)]
dx = [1,0,-1,0] # 4방향 이동위해 x가 1일 경우 y는 0
dy = [0,1,0,-1]
dp = [[-1 for _ in range(m)] for _ in range(n)] # -1로 초기화한이유는 방문을 안한곳이면 -1로 초기화 방문을 하면 0으로 바꿔줌

def dfs(x, y): # 깊이 우선탐색
    if x == n-1 and y == m-1: # 맨밑에 도착하면 1로 시작
        return 1
    if dp[x][y] != -1: # 이미 방문했던 곳이면 dp값 반환 (메모이제이션)
        return dp[x][y]
    
    dp[x][y] = 0 # 방문 먼저 하고
    for i in range(4): # 4방향으로 방문
        nextX = x + dx[i]
        nextY = y + dy[i]
        if nextX >= 0 and nextX < n and nextY >=0 and nextY < m : # 맵의 인덱스를 안 벗어나고
            if arr[nextX][nextY] < arr[x][y]: # 다음 값이 현재 값보다 작으면(내리막 길이면)
                dp[x][y] += dfs(nextX, nextY) # 0에다가 dfs 반환된 값 저장
    return dp[x][y] #dp반환
print(dfs(0,0))