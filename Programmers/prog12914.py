# 프로그래머스 연습문제 - 멀리 뛰기
# https://programmers.co.kr/learn/courses/30/lessons/12914

from itertools import combinations

# 콤비네이션으로 풀기 -> 시간초과 뜸


def solution(n):
    answer = 0
    two = n//2
    one = n % 2
    if n == 1:
        return 1
    while 1:
        answer += len(list(combinations(range(two+one), two)))
        if two != 0:
            two -= 1
            one += 2
        else:
            break

    return answer % 1234567


# print(solution(5))

# dp로 풀기
def solution2(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    dp = [0]*n
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n):
        dp[i] = dp[i-2] + dp[i-1]
    return dp[n-1] % 1234567


print(solution2(5))
