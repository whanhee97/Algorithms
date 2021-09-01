# 프로그래머스 완전탐색 - 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations


def isPrime(n):
    check = True
    if n != 2 and n % 2 == 0:
        return False
    if n == 1 or n == 0:
        return False
    for i in range(2, n):
        if n % i == 0:
            check = False
    return check


def solution(numbers):
    answer = 0
    n_list = list(numbers)
    com_list = []
    for i in range(1, len(numbers)+1):
        com_list.extend(list(map(''.join, permutations(n_list, i))))
    set_com = set(map(int, com_list))
    for n in set_com:
        if isPrime(int(n)):
            answer += 1
    return answer


print(solution("002"))
