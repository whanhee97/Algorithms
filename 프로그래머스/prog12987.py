# Summer/Winter Coding(~2018) - 숫자 게임
# https://programmers.co.kr/learn/courses/30/lessons/12987

def solution(A, B):
    answer = 0
    sortedA = sorted(A)
    sortedB = sorted(B)
    for i in sortedA:
        while sortedB:
            temp = sortedB.pop(0)
            if temp > i:
                answer += 1
                break
    return answer


A = [2, 2, 2, 2]
B = [1, 1, 1, 1]
print(solution(A, B))
