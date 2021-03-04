# 2019 카카오 개발자 겨울 인턴십 / 튜플
# https://programmers.co.kr/learn/courses/30/lessons/64065?language=python3
import sys
input = sys.stdin.readline

def solution(s):
    answer = []
    ss = s[2:-2].split("},{")
    ss.sort(key = len)
    for i in ss:
        arr = i.split(",")
        for a in arr:
            if int(a) not in answer:
                answer.append(int(a))
    return answer

s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"

print(solution(s))