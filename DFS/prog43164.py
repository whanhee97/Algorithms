# 프로그래머스 깊이/너비 우선 탐색(DFS/BFS) - 여행경로
# https://programmers.co.kr/learn/courses/30/lessons/43164

def dfs(tickets, answer, history, visit, frm, depth):
    history += frm + ','
    if depth == len(tickets):
        answer.append(history[:])
    for i in range(len(tickets)):
        if tickets[i][0] == frm and visit[i] == 0:
            visit[i] = 1
            dfs(tickets, answer, history[:], visit, tickets[i][1], depth+1)
            visit[i] = 0


def solution(tickets):
    answer = []
    visit = [0]*len(tickets)
    dfs(tickets, answer, '', visit, "ICN", 0)
    answer.sort()
    answer = answer[0].split(',')[:-1]
    return answer


tickets = [["ICN", "SFO"], ["ICN", "ATL"], [
    "SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
print(solution(tickets))
