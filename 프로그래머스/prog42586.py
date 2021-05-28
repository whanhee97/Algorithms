# 프로그래머스 스택/큐 - 기능개발
# https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []
    leftdays = []
    for i in range(len(progresses)):
        left = int((100 - progresses[i])/speeds[i]) if (100 - progresses[i]
                                                        ) % speeds[i] == 0 else int((100 - progresses[i])//speeds[i]) + 1
        leftdays.append(left)

    temp = []
    for t in leftdays:
        if len(temp) == 0:
            temp.append(t)
        else:
            if max(temp) >= t:
                t = max(temp)
                temp.append(t)
            else:
                temp.append(t)

    dict = {}
    for v in temp:
        if dict.get(v):
            dict[v] += 1
        else:
            dict[v] = 1

    dict = sorted(dict.items())
    answer = list(map(lambda x: x[1], dict))
    return answer


solution([93, 30, 55], [1, 30, 5])
