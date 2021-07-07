# 프로그래머스 해시 - 베스트앨범
# https://programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []
    g_dict = dict()
    for i in range(len(genres)):
        if genres[i] in g_dict:
            g_dict[genres[i]].append(i)
        else:
            g_dict[genres[i]] = []
            g_dict[genres[i]].append(i)

    print(g_dict)
    p_dict = dict()
    for i in g_dict.items():
        Sum = 0
        for j in i[1]:
            Sum += plays[j]
        p_dict[i[0]] = Sum
    sortedGenres = sorted(p_dict, key=lambda x: p_dict[x], reverse=True)
    for i in range(len(sortedGenres)):
        if len(g_dict[sortedGenres[i]]) == 1:
            answer.append(g_dict[sortedGenres[i]][0])
        else:
            g_dict[sortedGenres[i]].sort(key=lambda x: (
                plays[x], -x), reverse=True)
            answer.append(g_dict[sortedGenres[i]][0])
            answer.append(g_dict[sortedGenres[i]][1])

    return answer


genres = ["classic", "classic", "classic", "pop"]
plays = [500, 150, 800, 2500]
solution(genres, plays)
