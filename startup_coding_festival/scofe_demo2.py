import sys
input = sys.stdin.readline
t = int(input())
nms = [list(map(int,input().split())) for _ in range(t)]
for nm in nms:
    total = nm[0] + nm[1]
    n_q = nm[0]//5
    print(min(n_q,total//12))
