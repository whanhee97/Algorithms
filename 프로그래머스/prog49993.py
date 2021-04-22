# Summer/Winter Coding(~2018) - 스킬트리
# https://programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    answer = 0
    d = dict()
    for idx, one in enumerate(skill):
        d[one] = idx
    for s in skill_trees:
        arr = []
        for c in list(s):
            if c in d:
                arr.append(d[c])
        isOk = True
        for i in range(len(arr)):
            if i != arr[i]:
                isOk = False
        if isOk:
            answer += 1
    return answer


def solution2(skill, skill_tree):
    answer = 0
    for i in skill_tree:
        skillist = ''
        for z in i:
            if z in skill:
                skillist += z
        if skillist == skill[0:len(skillist)]:
            answer += 1
    return answer
