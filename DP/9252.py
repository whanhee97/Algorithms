#백준 9252 - LCS 2 // 문자열 DP문제
import sys
input = sys.stdin.readline
arr1 = input().strip() # 공백문자 제거
arr2 = input().strip()
dp = [[0 for _ in range(len(arr2)+1)]for _ in range(len(arr1)+1)]
for i in range(1,len(arr1)+1): 
    for j in range(1,len(arr2)+1):
        if arr1[i-1] == arr2[j-1]: # 2차원으로 나열 해서 두 개 문자 같으면 대각선 위 dp값 +1
            dp[i][j] = dp[i-1][j-1]+1
        else: # 다르면 위랑 왼쪽 dp값 둘중 큰 거
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])
print(dp[-1][-1]) # 여기 까지가 LCS 알고리즘 알아두기!

# 여기서 부터 역추적 // 구한 dp맵을 가지고 두 개 문자가 같으면 대각선 이동하고 문자 저장, 다르면 위쪽과 왼쪽 중 더 큰 쪽으로 이동
if dp[-1][-1] != 0:
    ans = []
    x, y = len(arr1),len(arr2)
    while x >= 1 and y >= 1:
        if arr1[x-1] == arr2[y-1]:
            ans.append(arr1[x-1])
            x -= 1
            y -= 1
        else:
            if dp[x-1][y] >= dp[x][y-1]:
                x -= 1
            else:
                y -= 1
    newstr = ''
    for s in range(len(ans)):
        newstr += ans.pop()
    print(newstr)
