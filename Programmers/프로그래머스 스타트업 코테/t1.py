def solution(code, day, data):
    answer = []
    nData = []
    for d in data:
        nd = d.split(' ')
        if nd[1].find(code) != -1:
            if nd[2].find(day) != -1:
                answer.append(nd)
    answer.sort(key=lambda x: x[2])
    newAnswer = []
    for a in answer:
        newAnswer.append(int(a[0][6:]))
    return newAnswer
