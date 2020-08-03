#백준 9095 - 1,2,3 더하기
import sys
input = sys.stdin.readline
n = int(input())
answer = []
d = [0 for _ in range(12)]
def dp(x):
    d[1] = 1
    d[2] = 2
    d[3] = 4
    for i in range(4,12):
        d[i] = d[i-3]+d[i-2]+d[i-1] # d[4]의 경우 '1'+d[3]+'2'+d[2]+'3'+d[1] : 각각의 경우의 수에 맨앞에 1,2,3이 붙는 경우의 수가 같다 ex) d[3] = 111 12 3 -> 1111 112 13
    return d[x]
for _ in range(n):
    answer.append(int(input()))
for j in range(n):
    print(dp(answer[j]))