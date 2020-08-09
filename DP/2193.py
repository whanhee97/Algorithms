# 백준 2193 - 이친수
import sys
input = sys.stdin.readline
n = int(input())
d = [0 for _ in range(n+1)]
d[1] = 1
if n>=2:
    d[2] = 1
    for i in range(3,n+1):
        d[i] = d[i-1] + d[i-2]
print(d[n])