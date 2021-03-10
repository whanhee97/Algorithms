# 백준 1931 - 회의실
# https://www.acmicpc.net/problem/1931

import sys
input = sys.stdin.readline

N = int(input())
times = []
for _ in range(N):
    times.append(tuple(map(int, input().split())))

times.sort(key = lambda x : (x[1],x[0]))
cnt = 0
lastTime = 0
for time in times:
    if time[0] >= lastTime:
        lastTime = time[1]
        cnt += 1

print(cnt)