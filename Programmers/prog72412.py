# 프로그래머스 2021 KAKAO BLIND RECRUITMENT - 순위 검색
# https://programmers.co.kr/learn/courses/30/lessons/72412

from itertools import combinations


def solution(info, query):
    answer = []
    db = {}
    # 모든 경우의 수 만들기
    for i in info:
        temp = i.split(' ')
        condition = temp[:-1]
        score = int(temp[-1])
        for n in range(5):
            combi = list(combinations(range(4), n))  # (0,1,2,3) 중에서 n개 뽑기
            for c in combi:
                temp_con = condition[:]
                for switch in c:
                    temp_con[switch] = '-'
                key = ''.join(temp_con)
                # 같은 것들 그룹화 해서 딕셔너리에 넣어 주기
                if key in db:
                    db[key].append(score)  # 문자열이 있으면 그 그룹에 점수 추가하고
                else:
                    db[key] = [score]  # 문자열이 없으면 그룹을 만들고 점수 추가
    # 딕셔너리 모든 값들 그룹별로 정렬
    for value in db.values():
        value.sort()

    for q in query:
        # 쿼리 파싱
        temp_q = q.replace('and ', '').split(' ')
        q_condition = ''.join(temp_q[:-1])
        q_score = int(temp_q[-1])

        # 쿼리가 딕셔너리에 존재하면
        if q_condition in db:
            data = db[q_condition]
            if len(data) > 0:
                start, end = 0, len(data)     # lower bound 알고리즘 통해 인덱스 찾고,
                while start != end and start != len(data):
                    if data[(start + end) // 2] >= q_score:
                        end = (start + end) // 2
                    else:
                        start = (start + end) // 2 + 1
                answer.append(len(data) - start)      # 해당 인덱스부터 끝까지의 갯수가 정답
        else:
            answer.append(0)

    return answer


info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]

print(solution(info, query))
