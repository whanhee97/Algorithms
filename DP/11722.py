# 백준 11722 - 가장 긴 감소하는 부분 수열
import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
d = [1 for _ in range(n)] # 자기 자신을 포함하므로 1부터 시작 
for i in range(n): # 이때 d는 자신a[i]과 이전의 수들a[j]를 모두 비교하여서 자신보다 작으면 패스하고 크면 d[i]와 d[j]가 같을 경우 +1 해준다 d[j]가 더 작으면 갱신할 필요가 없으므로 패스 
    for j in range(i+1):
        if a[i] < a[j] and d[i] <= d[j]:
            d[i] += 1
Max = 0
for M in d:
    if M >= Max:
        Max = M
print(Max)