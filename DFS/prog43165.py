# 프로그래머스 깊이/너비 우선 탐색(DFS/BFS) - 타겟 넘버
# https://programmers.co.kr/learn/courses/30/lessons/43165
answer = 0


def solution(numbers, target):
    global answer
    result = 0
    idx = -1
    dfs(numbers, target, result, idx)
    return answer


def dfs(numbers, target, result, idx):
    global answer
    if idx+1 == len(numbers):
        if result == target:
            answer += 1
        return
    dfs(numbers, target, result + numbers[idx+1], idx+1)
    dfs(numbers, target, result - numbers[idx+1], idx+1)


numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))
