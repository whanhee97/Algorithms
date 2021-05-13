# 프로그래머스 힙 - 더 맵게
# https://programmers.co.kr/learn/courses/30/lessons/42626
import heapq


def solution(scoville, K):
    answer = 0
    scoville.sort()
    while 1:
        if scoville[0] >= K:
            return answer
        if len(scoville) == 1:
            break
        first = scoville.pop(0)
        second = scoville.pop(0)
        heapq.heappush(scoville, (first + second*2))
        answer += 1

    return -1


scoville = [7, 1, 5, 6]
K = 14

print(solution(scoville, K))
