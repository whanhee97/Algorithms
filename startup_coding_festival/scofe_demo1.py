# 스코페 모의테스트1
# import sys
# input = sys.stdin.readline

# n,k = map(int, input().split())
# arr = list(map(int, input().split()))
# arr.sort()
# cnt = 0
# while len(arr) != 1:
#     try:
#         for i in range(k):
#             arr[i] = arr[0]
#     except:
#         cnt += 1
#         break
#     arr = set(arr)
#     arr = list(arr)
#     cnt += 1

# print(cnt)

import sys
import math
n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
# 제일 작은수로 전부 바꾸는 거나 그냥 아무숫자로 통일 하는 거나 결국 같은거 아닌가?
cnt = 1
box = k # 처음에 k개 만큼 들어가고 1개 카운트
while True:
    if(box >=n): break # 박스 안에 개수가 전체 개수보다 작으면 반복
    box += k-1 # 다음 부터는 k-1개씩 박스에 추가함(1개는 겹쳐야 하므로)
    cnt += 1

print(cnt)