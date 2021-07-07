# 프로그래머스 - 예상 대진표
# https://programmers.co.kr/learn/courses/30/lessons/12985
def solution(n, a, b):
    answer = 0
    stop = False
    while 1:
        answer += 1
        if abs(a-b) == 1 and max(a, b) % 2 == 0:
            stop = True
        n = n/2
        a = a/2 if (a % 2 == 0) else a//2+1
        b = b/2 if (b % 2 == 0) else b//2+1

        if stop:
            break

    return answer


n = 8
a = 4
b = 7
print(solution(n, a, b))
