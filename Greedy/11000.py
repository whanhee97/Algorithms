# 백준 - 강의실 배정
# https://www.acmicpc.net/problem/11000

import heapq
import sys
input = sys.stdin.readline

n = int(input())
stList = []
for _ in range(n):
    stList.append(list(map(int, input().split())))
stList.sort(key=lambda x: x[0])  # 시작시간을 오름차순으로
start, end = heapq.heappop(stList)
classroom = []  # 종료시간을 오름 차순으로 종료시간만 저장
classroom.append(end)
while stList:
    start, end = heapq.heappop(stList)  # 두번째로 시작하는 시간부터 꺼냄
    if start < classroom[0]:  # 배정안된 수업의 시작이 가장 일찍끝나는 수업의 끝보다 작으면
        heapq.heappush(classroom, end)  # 끝나는 시간 추가하고 정렬(수업 개설)
    else:  # 배정안된 수업의 시작이 가장 일찍끝나는 수업의 끝보다 늦게 시작하면
        heapq.heappop(classroom)  # 가장 일찍 끝나는 수업 뺴고
        heapq.heappush(classroom, end)  # 그 교실을 이어감


print(len(classroom))
