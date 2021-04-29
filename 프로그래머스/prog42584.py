# 프로그래머스 스택/큐 - 주식가격
# https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = []
    answer.append(0)
    check = [0 for _ in range(len(prices))]
    for i in range(1, len(prices)):
        answer.append(0)
        for j in range(len(answer)-1):
            if prices[i] >= prices[j] and check[j] == 0:
                answer[j] += 1
            elif check[j] == 0:
                check[j] = 1
                answer[j] += 1

    return answer


prices = [4, 3, 4, 4, 2]
print(solution(prices))
