from collections import deque


def solution(t, r):
    answer = []
    waitingQ = []
    nowTurn = []
    arr = []
    for i in range(len(t)):
        arr.append((t[i], r[i], i))

    arr.sort(key=lambda x: (x[0], x[1]))
    maxTime = max(t)
    for time in range(maxTime+1):
        for a in arr:
            if a[0] == time:
                waitingQ.append(a)
        if len(waitingQ) != 0:
            waitingQ.sort(key=lambda x: x[1])
            answer.append(waitingQ.pop(0)[2])
            continue
    waitingQ.sort(key=lambda x: x[1])
    while waitingQ:
        answer.append(waitingQ.pop(0)[2])
    return answer


t = [2, 2, 2, 1, 3, 5]
r = [0, 1, 2, 3, 4, 5]
print(solution(t, r))
