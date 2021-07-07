# Summer/Winter Coding(~2018) - 스킬트리
# https://programmers.co.kr/learn/courses/30/lessons/49993

# 처음 푼 방식
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

# 다른 사람이 푼 방식


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

# 2회차때 푼 방식


def solution3(skill, skill_trees):
    answer = 0
    for st in skill_trees:
        check = True
        idxarr = []
        for s in skill:
            if s in st:
                idxarr.append(st.index(s))
            else:
                idxarr.append(27)
        for i in range(len(idxarr)-1):
            if idxarr[i] > idxarr[i+1]:
                check = False
                break
        if check:
            answer += 1
    return answer
