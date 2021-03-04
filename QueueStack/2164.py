# 백준 2164 - 카드2
import sys
from collections import deque # 큐를 쓸땐 deque을 쓰자 훨씬 빠르다
input = sys.stdin.readline
q=deque()
n = int(input())
for i in range(1,n+1):
    q.append(i)
while len(q) != 1:
    q.popleft()
    temp = q.popleft()
    q.append(temp)
print(q[0])