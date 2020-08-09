#백준 2579 - 계단 오르기
import sys
input = sys.stdin.readline
n = int(input())
stair = []
stair.append(0)
d = [0 for _ in range(n+1)]  #직관성을 위해 0번 인덱스를 시작으로함
for i in range(n):
    stair.append(int(input()))
d[1] = stair[1]
if n>=2: # 이거 안 붙여줘서 런타임 에러남 n = 1일때 stair[2]는 없으므로 
    d[2] = stair[1]+stair[2]
    for i in range(3,n+1):
        d[i] = max(d[i-2]+stair[i],d[i-3]+stair[i-1]+stair[i])
print(d[-1])