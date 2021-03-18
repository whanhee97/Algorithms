# 백준 1700 - 멀티탭 스케줄링
# https://www.acmicpc.net/problem/1700

import sys
input = sys.stdin.readline

n,k = map(int,input().split())
referenceStr = list(map(int,input().split())) 
plug = [0 for _ in range(n)] # 코드 꽂는 곳
cnt = 0
for i in range(k):
    check = False
    for j in range(n):
        if plug[j] == 0 or plug[j] == referenceStr[i]: #코드가 안 꽂혀 있거나 같은 기기이면
            plug[j] = referenceStr[i] # 코드 꽂고 체크
            check = True
            break
    if check: #체크되면 다음으로 넘어감(코드를 뺼 필요 없다는 얘기)
        continue

    maxDistance = 0 #가장 순서가 먼 기기를 찾기위한 변수 
    maxIdx = 0 # 그 기기의 인덱스값을 얻기 위한 변수
    for j in range(n): # 순서중에 젤 멀리 있는 순서 찾기
        try: # 현재꺼의 다음 순서부터 해서 만약에 있으면 인덱스로 거리 계산
            if maxDistance < referenceStr[i+1:].index(plug[j]):
                maxDistance = referenceStr[i+1:].index(plug[j])
                maxIdx = j
        except: # 없으면 index()가 에러 나므로 (앞으로 쓸일이 없으므로 그 자리 코드를 뽑으면 됨)
            maxDistance = 101
            maxIdx = j        
    plug[maxIdx] = referenceStr[i] # 가장 순서가 먼 기기가 꽂혀있는 코드를 뽑고 현재 기기를 꽂음
    cnt += 1

print(cnt)



#### 실패 (어느 케이스에서 오류나는지 모르겠음 ㅠㅠ)####

# plug = [[0,101] for _ in range(n)] # 코드 꽂는 곳
# cnt = 0

# while True:
#     check = False
#     if len(referenceStr) == 0:
#         break
    
#     r = referenceStr.pop(0) # 한개 꺼내서
#     if r in referenceStr: # 뒤에 그게 있으면 
#         distance = referenceStr.index(r) # 거리를 저장
#         temp = [r,distance]
#     else:
#         temp = [r,101] # 없으면 최대거리 저장

#     for i in range(len(plug)):
#         if plug[i][0] == r:
#             plug[i] = temp
#             check = True
#             break
#     if check:
#         continue
#     maxDistance = 0
#     maxIdx = 0
#     for i in range(len(plug)):
#         if maxDistance < plug[i][1]:
#             maxDistance = plug[i][1]
#             maxIdx = i
    
#     plug[maxIdx] = temp
#     cnt += 1
#     for p in plug: # 코드의 꽂혀 있는 거리값을 1만큼 낮춰야함. 전체 배열에서 하나씩 빼므로 가까워지니까
#         p[1] -= 1

# if cnt-n<0:
#     answer = 0
# else:
#     answer = cnt - n
# print(answer)


##### 밑에는 운영체제 수업때 배운 optimal 방법으로 품 (정답이지만 코드가 너무 길다)#####
# def isExist(frames, num ,n):
#     for i in range(n):
#         if frames[i][0] == num:
#             return i
#     return -1

# def mostFar(frames,currentIndex,referenceStr,n):
#     for i in range(n):# 프레임 4개를 검사해서 각각의 거리를 저장
#         distance = 1
#         check = False
#         for j in range(currentIndex+1,len(referenceStr)):
#             if(referenceStr[j] == frames[i][0]): #값과 일치하는게 있으면 멈추고 거리 저장
#                 frames[i][1] = distance 
#                 check = True
#                 break
#             distance +=1
#         if not check:
#             frames[i][1] = 100 #없으면 거리를 100으로 저장
    
#     maxDistance = 0
#     mostFarIndex = 0
#     for i in range(n-1,-1,-1): #마지막 프레임부터 검사해서 가장 거리가 먼 프레임 인덱스 저장
#         if frames[i][1] >= maxDistance:
#             maxDistance = frames[i][1]
#             mostFarIndex = i
    
#     return mostFarIndex # 제일 먼 프레임의 인덱스를 반환

# def OptimalInsert(frames,num,currentIndex,referenceStr,n):
#     # 가장 멀리있는 프레임의 인덱스를 구함
#     MaxIndex = mostFar(frames,currentIndex,referenceStr,n)
#     # 가장 멀리있는 곳에 num을 넣음
#     frames[MaxIndex][0] = num

# def Optimal(referenceStr,n):
#     OptimalFrames = [[0,0] for _ in range(n)]# 첫번쨰는 값, 두번쨰는 얼마나 멀리있는지
#     pageFault = 0
    
#     for i in range(len(referenceStr)):
#         result = isExist(OptimalFrames,referenceStr[i],n)
#         if result == -1: # 존재하지 않으면
#             OptimalInsert(OptimalFrames,referenceStr[i],i,referenceStr,n)
#             pageFault +=1
        
#     return pageFault

# print(Optimal(referenceStr,n)-n) #페이지폴트는 집어 넣을 때도 포함되므로 프레임에 집어넣을때(n)를 빼줘야함