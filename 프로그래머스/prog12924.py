# 프로그래머스 실력체크 lv.2 - 숫자의 표현
# https://programmers.co.kr/learn/courses/30/lessons/12924
def solution(n):
    answer = 0
    for i in range(n//2 + 1, 0, -1):
        Sum = 0
        for j in range(i, 0, -1):
            Sum += j
            if Sum == n:
                answer += 1
                break
            if Sum > n:
                break
    return answer+1


solution(15)
