#백준 2309 - 일곱 난쟁이
# https://www.acmicpc.net/problem/2309
import sys
input = sys.stdin.readline

arr = []
def getIJ(arr):
    for i in range(8):
        for j in range(i+1,9):
            if total(i,j,arr) == 100:
                return (i,j)

def total(a1,a2,arr):
    sum = 0
    for i in range(9):
        if(i != a1 and i != a2):
            sum += arr[i]
    return sum

answer = []
ij =getIJ(arr)
i = ij[0]
j = ij[1]
for a in range(9):
    if a != i and a != j:
        answer.append(arr[a])
answer.sort()
#print()
for x in answer:
    print(x)
                


##############################################

# for _ in range(9):
#     arr.append(int(input()))

# total = sum(arr)
# arr.sort()
# for i in range(9):
#     for j in range(i+1,9):
#         if (total - arr[i] - arr[j]) == 100:
#             for k in range(9):
#                 if k !=i and k !=j:
#                     print(arr[k])
#             exit()