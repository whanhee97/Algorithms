#백준 11049 - 행렬 곱셈 순서
import sys
import math
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

for gap in range(1,n): # dp[start][end] 일때 start와 end의 차이 1부터 3까지 기록한다는 뜻 ex) dp[1][2], dp[2][3], dp[3][4]
    start = 0 #스타트 0부터 시작
    while start + gap < n: 
        end = start+gap
        dp[start][end] = math.inf # 처음에 가장 큰 값을 넣어 놓고
        for mid in range(start,end): # mid를 start~end까지 해서 가장 작은 값 골라내는 과정 
            dp[start][end] = min(dp[start][end], dp[start][mid] + dp[mid+1][end] + arr[start][0]*arr[mid][1]*arr[end][1] )
        start += 1
print(dp[0][n-1])
  