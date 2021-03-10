# 백준 1449 - 수리공 항승
# https://www.acmicpc.net/problem/1449

import sys
input = sys.stdin.readline

N,L = map(int, input().split())
locations = list(map(int, input().split()))
locations.sort()
cnt = 0
last = 0 # 마지막으로 막은 위치 (테이프의 길이를 고려)
for hole in locations:
    if hole > last: # 구멍이 마지막으로 막은 위치보다 오른쪽에 있으면
        cnt += 1 # 테이프를 추가하고
        last = hole + (L-1) # 마지막으로 막은 위치를 현재 구멍 + 테이프의 길이(-1)로 바꿔준다
print(cnt)

###내가 푼 방식###
# check = [0 for _ in range(N)]
# cnt = 1

# for i in range(N-1): # i : 0~뒤에서 두번째 까지 탐색
#     if check[i] != 1: # i 체크 됐는지 확인
#         for j in range(i+1,N): # j : i담꺼 부터 해서 빼준다음에 L-1보다 크면(테이프길이가 초과 됐으므로) cnt를 추가해주고 check에다가 표시해줌
        
#             if locations[j] - locations[i] > L-1 : 
#                 cnt += 1
#                 for k in range(i,j):
#                     check[k] = 1
#                 break

# print(cnt)
