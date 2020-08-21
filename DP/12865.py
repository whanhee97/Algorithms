#백준 12865 - 평범한 배낭 // 짐을 쪼갤 수 없는 배낭 문제 (0-1 Knapsack Problem) - 이 경우 DP 사용, 쪼갤 수 있는 경우는 그리디 사용
import sys
input = sys.stdin.readline
ip = list(map(int, input().split()))
n = ip[0]
w = ip[1]
arr = [list(map(int,input().split())) for _ in range(n)]
dp = [[0 for _ in range(w+1)] for _ in range(n+1)] 
for i in range(1,n+1):
    for j in range(1,w+1): #배낭의 무게가 1 ~ w까지 하나씩 늘어남
        if arr[i-1][0] > j: #i번쨰 물건 무게가 지금 배낭의 무게보다 무거우면 넣을 수 없으므로 // dp를 편의상 1부터 시작했으므로 i-1이 i번째
            dp[i][j] = dp[i-1][j] #위에꺼(현재 물건 안들어갔을때 최적값) 그대로 들고옴
        else: # 배낭의 무게가 더 크다면
            dp[i][j] = max(arr[i-1][1] + dp[i-1][j-arr[i-1][0]], dp[i-1][j]) #(현재 물건의 가치 + 현재물건의 무게를 제외하고 최적값) // 위에꺼(현재 물건 안들어갔을때 최적값) 비교
print(dp[-1][-1])

# 점화식 기억하기 P[i][w] = P[i-1][w] // if w[i] > w //(i번쨰 물건 무게가 지금 배낭의 무게보다 무거우면 넣을 수 없으므로 안 넣고 위에꺼 최적값 가져옴) 
#                        = max(v[i] + P[i-1][w-w[i]] , p[i-1][w]) // else // 배낭의 무게가 더 무거우면 i번째 물건 넣을 때랑 안 넣을 때 비교
# (넣을때는 i번째 물건제외한 최적값, 즉 P[i-1][w-w[i]] 에 i번째 물건의 가치를 더해줘야함)