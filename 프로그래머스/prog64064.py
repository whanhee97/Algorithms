# 프로그래머스 - 불량 사용자
# https://programmers.co.kr/learn/courses/30/lessons/64064


from itertools import permutations


def check(users, banned_id):
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False
        for j in range(len(users[i])):
            if users[i][j] == banned_id[i][j] or banned_id[i][j] == '*':
                continue
            else:
                return False
    return True


def solution(user_id, banned_id):
    user_permutations = permutations(user_id, len(banned_id))
    banned_set = []
    for users in user_permutations:
        if not check(users, banned_id):
            continue
        else:
            if users not in banned_set:
                banned_set.append(set(users))

    return len(banned_set)


print(solution(	["frodo", "fradi", "crodo", "abc123", "frodoc"], [
      "fr*d*", "*rodo", "******", "******"]))
