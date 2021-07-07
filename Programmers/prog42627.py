# 프로그래머스 힙 - 디스크 컨트롤러
# https://programmers.co.kr/learn/courses/30/lessons/42627
def solution(jobs):
    answer = 0
    n = len(jobs)
    jobs.sort(key=lambda x: (x[0], x[1]))
    que = []
    while jobs:
        if len(que) == 0:
            que.append(jobs.pop(0))
        out = 0
        while que:
            item = que.pop(0)
            if out == 0:
                out += item[0]+item[1]
            else:
                out += item[1]
            answer += out - item[0]
            while jobs:
                if jobs[0][0] <= out:
                    que.append(jobs.pop(0))
                else:
                    break
            que.sort(key=lambda x: x[1])

    return int(answer/n)


print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [
      20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]), 72)
# print(solution([[0, 10], [2, 12], [9, 19], [15, 17]]), 25)
# print(solution([[0, 3], [1, 9], [2, 6]]), 9)
# print(solution([[0, 1]]), 1)
# print(solution([[1000, 1000]]), 1000)
# print(solution([[0, 1], [0, 1], [0, 1]]), 2)
# print(solution([[0, 1], [0, 1], [0, 1], [0, 1]]), 2)
# print(solution([[0, 1], [1000, 1000]]), 500)
# print(solution([[100, 100], [1000, 1000]]), 500)
# print(solution([[10, 10], [30, 10], [50, 2], [51, 2]]), 6)
# print(solution([[0, 3], [1, 9], [2, 6], [30, 3]]), 7)
