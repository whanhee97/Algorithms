# Summer/Winter Coding(~2018) - 방문 길이
# https://programmers.co.kr/learn/courses/30/lessons/49994
import copy


def solution(dirs):
    answer = 0
    curPos = [5, 5]
    histories = []
    for command in dirs:
        prePos = copy.deepcopy(curPos)
        if command == 'D':
            if curPos[1]+1 <= 10:
                curPos[1] += 1
                if [prePos, curPos] not in histories:
                    histories.append(
                        [copy.deepcopy(prePos), copy.deepcopy(curPos)])
                    histories.append(
                        [copy.deepcopy(curPos), copy.deepcopy(prePos)])
                    answer += 1
        elif command == 'U':
            if curPos[1]-1 >= 0:
                curPos[1] -= 1
                if [prePos, curPos] not in histories:
                    histories.append(
                        [copy.deepcopy(prePos), copy.deepcopy(curPos)])
                    histories.append(
                        [copy.deepcopy(curPos), copy.deepcopy(prePos)])
                    answer += 1
        elif command == 'R':
            if curPos[0]+1 <= 10:
                curPos[0] += 1
                if [prePos, curPos] not in histories:
                    histories.append(
                        [copy.deepcopy(prePos), copy.deepcopy(curPos)])
                    histories.append(
                        [copy.deepcopy(curPos), copy.deepcopy(prePos)])
                    answer += 1
        else:
            if curPos[0]-1 >= 0:
                curPos[0] -= 1
                if [prePos, curPos] not in histories:
                    histories.append(
                        [copy.deepcopy(prePos), copy.deepcopy(curPos)])
                    histories.append(
                        [copy.deepcopy(curPos), copy.deepcopy(prePos)])
                    answer += 1
    return answer


dirs = "ULURRDLLU"
print(solution(dirs))


def solution2(dirs):
    s = set()
    d = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x, y, nx, ny))
            s.add((nx, ny, x, y))
            x, y = nx, ny
    return len(s)//2
