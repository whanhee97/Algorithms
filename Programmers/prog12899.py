# 프로그래머스 - 124 나라의 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12899
def solution(n):
    numDict = {'1': '1', '2': '2', '3': '4', '0': '4'}
    answer = ''
    answerStack = []
    num = n
    while 1:
        answerStack.append(numDict[str(num % 3)])
        if num <= 3:
            break
        if num % 3 == 0:
            num = (num // 3) - 1
        else:
            num = num // 3

    while answerStack:
        answer += answerStack.pop()

    return answer


print(solution(12))
