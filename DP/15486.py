#백준 15486 - 퇴사2
import sys
input = sys.stdin.readline
n = int(input())
arr = []
dp = [0 for _ in range(n+1)]
for _ in range(n):
    arr.append(tuple(map(int,input().split()))) 

# for i in range(n): //이렇게 하면 시간초과
#     temp = i
#     result = 0
#     while i < n-1:
#         result += arr[i][1]
#         i += arr[i][0]
#     if arr[n-1][0] == 1:
#         result += arr[n-1][1]
#     dp[temp] = result


#퇴사일 n+1 인데 여기서는 인덱스가 0부터 시작하므로 n을 퇴사일로 설정
for i in range(n-1,-1,-1):
    if i + arr[i][0] > n: # 상담이 퇴사 날짜 이후에 끝날때
        dp[i] = dp[i+1] #상담 안하기(다음날로 패스)
    else:
        dp[i] = max(dp[i+arr[i][0]]+arr[i][1], dp[i+1]) #max(상담끝나고 금액 + 현재금액 , 상담안할때)
Max = 0
for j in dp:
    if Max <= j:
        Max = j
print(Max)