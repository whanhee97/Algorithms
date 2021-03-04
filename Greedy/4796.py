# 백준 4796 - 캠핑
import sys
input = sys.stdin.readline
i=1
while 1:
    L,P,V = map(int,input().split())
    if L==0 and P==0 and V ==0:
        break
    answer = int(V/P)*L
    if V%P > L:
        answer += L
    else:
        answer += V%P
    print("Case {0}: {1}".format(i,answer))
    i += 1

