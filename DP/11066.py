#백준 11066 - 파일 합치기 // 행렬 곱셈 순서(11049)랑 똑같은 유형 - 둘 다 잘 보기
import sys
import math
input = sys.stdin.readline
testdata = int(input())
for i in range(testdata):
    n = int(input())
    files = list(map(int,input().split()))
    sum = [0 for _ in range(n+1)]
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for j in range(1,n+1):
        sum[j] = sum[j-1] + files[j-1] # sum[i]는 i까지 합
    
    for gap in range(1,n): # dp[start][end] 일때 start와 end의 차이 1부터 3까지 기록한다는 뜻 ex) dp[1][2], dp[2][3], dp[3][4]
        start = 1 #스타트 1부터 시작
        while start + gap <= n: 
            end = start+gap
            dp[start][end] = math.inf # 처음에 가장 큰 값을 넣어 놓고
            for mid in range(start,end): # mid를 start~end까지 해서 가장 작은 값 골라내는 과정 // dp[i][j] = min(dp[i][k]+dp[k+1][j]+sum(i~j)) k는 i~j-1까지
                dp[start][end] = min(dp[start][end], dp[start][mid] + dp[mid+1][end] + (sum[end]-sum[start-1]) )
            start += 1
    print(dp[1][n])
  
