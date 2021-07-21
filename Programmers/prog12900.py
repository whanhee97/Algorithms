# 프로그래머스 - 2 x n 타일링
# https://programmers.co.kr/learn/courses/30/lessons/12900

def solution(n):
    answer = 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    x = 1
    y = 2
    z = 0
    for i in range(2, n):
        z = x + y
        x = y
        y = z
    return z % 1000000007


print(solution(6))
