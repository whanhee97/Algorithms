def solution(clothes):
    answer = 1
    c_dict = dict()
    for c in clothes:
        if c[1] not in c_dict:
            c_dict[c[1]] = []
        c_dict[c[1]].append(c[0])
    for k in c_dict.keys():
        answer *= (len(c_dict[k])+1)
    return answer-1


clothes = [["yellowhat", "headgear"], [
    "bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
solution(clothes)
