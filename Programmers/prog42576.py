# 프로그래머스 - 완주하지 못한 선수
# https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    answer = ''
    dict_par = dict()
    for p in participant:
        dict_par[p] = 0
    for p in participant:
        dict_par[p] += 1

    for c in completion:
        dict_par[c] -= 1
    for p in participant:
        if dict_par[p] == 1:
            return p
    return answer


# print(solution(["mislav", "stanko", "mislav", "ana"],
 #     ["stanko", "ana", "mislav"]))

print(solution(["leo", "kiki", "eden"],
      ["eden", "kiki"]))
