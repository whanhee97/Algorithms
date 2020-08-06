#백준 1149 - RGB 거리
import sys
input = sys.stdin.readline
n = int(input())
rgb_input = []
for _ in range(n):
    rgb_input.append(tuple(map(int,input().split())))
a = [[0 for _ in range(3)] for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(3):
        a[i][j] = rgb_input[i-1][j]
# 여기까지 입력
d = [[0 for _ in range(3)] for _ in range(n+1)]

for i in range(1,n+1): # 3가지 상황을 고려해야함 마지막 칠하는 색 빨초파 별로 // i번째 집은 i-1번쨰 집의 최솟값 + i번째 색의값
    d[i][0] = min(d[i-1][1],d[i-1][2])+a[i][0] #레드 // i-1번째 초록을 칠했을때 최솟값, 파랑을 칠했을때 최솟값중 더 작은 값 + i번쨰에 빨강 칠한값
    d[i][1] = min(d[i-1][0],d[i-1][2])+a[i][1] #그린
    d[i][2] = min(d[i-1][0],d[i-1][1])+a[i][2] #블루
print(min(d[n][0],d[n][1],d[n][2])) # 빨초파중 마지막에 칠한 (n번째) 값 중 가장 작은 값