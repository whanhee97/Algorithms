# 프로그래머스 연습문제 - 거스름돈
# https://programmers.co.kr/learn/courses/30/lessons/12907

def solution(n, money):
    answer = 0
    dp = [0] * (n+1)
    dp[0] = 1
    for coin in money:
        for price in range(coin, n+1):
            dp[price] += dp[price - coin]

    return dp[n]


solution(5, [1, 2, 5])
