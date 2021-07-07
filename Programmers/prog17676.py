# 프로그래머스 - 추석 트래픽
# https://programmers.co.kr/learn/courses/30/lessons/17676

def solution(lines):
    answer = 0
    startNfinish = []
    for line in lines:
        arr = line.split(' ')
        res_time = arr[1].split(':')
        res_sec_f = float(res_time[0])*3600 + \
            float(res_time[1])*60 + float(res_time[2])
        res_sec_s = round(res_sec_f - float(arr[2][:-1]) + 0.001, 3)
        startNfinish.append([res_sec_s, res_sec_f])
    startNfinish.sort(key=lambda x: x[1])
    for i in range(len(startNfinish)):
        for j in range(2):
            cnt = 0
            start = startNfinish[i][j]
            for k in startNfinish:
                if k[0] > round(start+0.999, 3) or k[1] < start:
                    continue
                cnt += 1
            if answer <= cnt:
                answer = cnt
    return answer


lines = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
print(solution(lines))
