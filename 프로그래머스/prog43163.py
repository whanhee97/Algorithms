# 프로그래머스 DFS/BFS - 단어 변환
# https://programmers.co.kr/learn/courses/30/lessons/43163
from collections import deque


def canConvert(w1, w2):
    cnt = 0
    for i in range(len(w1)):
        if w1[i] == w2[i]:
            cnt += 1
    return True if cnt == len(w1)-1 else False


def solution(begin, target, words):
    if target not in words:
        return 0
    visit = [0 for _ in range(len(words))]
    q = deque()
    q.append((begin, 0))
    while q:
        w = q.popleft()
        if w[0] == target:
            return w[1]
        for i in range(len(words)):
            if canConvert(w[0], words[i]) and visit[i] == 0:
                q.append((words[i], w[1]+1))
    return 0


# begin = "hit"
# target = "cog"
# words = ["hot", "dot", "dog", "lot", "log", "cog"]
# print(solution(begin, target, words))
# print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 4)
# print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0)
# print(solution("hit", "hot", ["hot", "dot", "dog", "lot", "log"]), 1)
print(solution("1234567000", "1234567899", [
      "1234567800", "1234567890", "1234567899"]), 3)
# print(solution("hit", "cog", ["cog", "log", "lot", "dog", "hot"]), 4)
