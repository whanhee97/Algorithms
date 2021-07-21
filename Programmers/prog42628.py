# 프로그래머스 - 이중우선순위큐
# https://programmers.co.kr/learn/courses/30/lessons/42628

def solution(operations):
    answer = []
    q = []
    while operations:
        op = operations.pop(0)
        op2 = op.split(' ')
        command = op2[0]
        data = op2[1]
        if command == 'I':
            q.append(int(data))
            q.sort()
        elif command == 'D':
            if data == '1':
                if len(q) != 0:
                    q.pop(-1)
            else:
                if len(q) != 0:
                    q.pop(0)

    if len(q) == 0:
        answer = [0, 0]
    else:
        answer.append(q.pop(-1))
        answer.append(q.pop(0))

    return answer


solution(["I 7", "I 5", "I -5", "D -1"])
