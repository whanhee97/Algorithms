from collections import deque


def solution(maps):
    answer = -1
    q = deque()
    q.append([0, 0, 1])
    mx = [1, 0, -1, 0]
    my = [0, 1, 0, -1]
    while q:
        x, y, total = q.popleft()

        if x == len(maps)-1 and y == len(maps[0])-1:
            answer = total
            break
        for i in range(4):
            if x+mx[i] >= 0 and x+mx[i] < len(maps) and y+my[i] >= 0 and y+my[i] < len(maps[0]):
                if maps[x + mx[i]][y + my[i]] == 1:
                    q.append([x + mx[i], y + my[i], total+1])
                    maps[x + mx[i]][y + my[i]] = -1

    return answer


solution("baabaa")
