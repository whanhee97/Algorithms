# 프로그래머스 Summer/Winter Coding(~2018) - 소수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12977
from itertools import combinations


def solution(nums):
    answer = 0
    for a in combinations(nums, 3):
        sumNum = sum(a)  # 다 더한걸 가지고
        isPrime = True
        for i in range(2, sumNum):
            if sumNum % i == 0:
                isPrime = False
                break
        if isPrime:
            answer += 1

    return answer


nums = [1, 2, 7, 6, 4]

print(solution(nums))
