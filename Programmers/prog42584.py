# 프로그래머스 스택/큐 - 주식가격
# https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = [0]*len(prices)
    stack = []

    for i, price in enumerate(prices):
        # stack이 비었이면 false
        # 스택 마지막 값이 현재 가격보다 크면 -> 가격이 떨어졌다는 의미 -> pop
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    # for문 다 돌고 Stack에 남아있는 값들 pop
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j

    return answer


prices = [4, 3, 4, 4, 2]
print(solution(prices))
