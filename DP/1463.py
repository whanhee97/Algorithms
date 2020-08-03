#입력받기 예제
# import sys
# sys.setrecursionlimit(10000) # 재귀리미트를 설정(기본은 1000)
# input = sys.stdin.readline
# c = int(input())
# students = []
# for _ in range(n):
#     students.append(tuple(map(int,input().split())))
# import sys
# sys.setrecursionlimit(1000000) # 재귀리미트를 설정(기본은 1000)
# d =[[0 for _ in range(2)]for _ in range(1000000)]
# n = int(input())
# def dp(n):
#     d[0][0] = 1
#     d[1][0] = 2
#     d[2][0] = 7
#     d[2][1] = 0
#     for i in range(3,n+1):
#         d[i][1] = (d[i-3][0] + d[i-1][1])%1000000007
#         d[i][0] = (2*d[i-1][0]+3*d[i-2][0]+2*d[i][1])%1000000007
#     return d[n][0]
# print(dp(n))

#백준1463 - 1로 만들기(DP)
#점화식을 생각해보면 n은 1) n-1에 한 번 더 연산을 했거나 2) n/2에 한 번 더 연산을 했거나 3) n/3에 한 번 더 연산을 헀거나 이므로 아래와 같은 식이 나온다
import sys
input = sys.stdin.readline
n = int(input())
d = [0 for _ in range(1000001)]
d[1] = 0
for i in range(2,1000001):
    d[i] = d[i-1] + 1
    if i%2==0 :
        d[i] = min(d[i//2]+1,d[i-1] + 1) # //써준이유는 /을 쓸경우 float로 인식해서 소수점을 버려주는 //사용
    if i%3==0 :
        d[i] = min(d[i//3]+1,d[i-1] + 1)
print(d[n])
