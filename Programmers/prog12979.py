# Summer/Winter Coding(~2018) - 기지국 설치
# https://programmers.co.kr/learn/courses/30/lessons/12979
from math import ceil


def solution(n, stations, w):
    answer = 0
    start = 0
    for s in stations:
        left = (s-1)-w  # 전파 범위중 가장 왼쪽을 left라고 함
        # left - start는 전파 범위에 안들어 가는 구간이고 1+2*w는 송신탑 하나의 최대범위임
        answer += ceil((left - start) / (1+2*w))
        start = s+w
    answer += ceil((n - start) / (1+2*w))  # 마지막 스타트에서 끝까지 구간
    return answer


n = 16
stations = [9]
w = 2
print(solution(n, stations, w))
