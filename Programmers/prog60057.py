# 프로그래머스 - 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = len(s)
    for step in range(1, len(s)//2+1):
        result = ""
        tmp = s[0:step]
        cnt = 1
        for j in range(step, len(s), step):
            if tmp == s[j:j+step]:
                cnt += 1
            else:
                result += str(cnt) + tmp if cnt > 1 else tmp
                tmp = s[j:j+step]
                cnt = 1
        result += str(cnt) + tmp if cnt > 1 else tmp
        answer = min(answer, len(result))
    return answer


s = "ababcdcdababcdcd"
print(solution(s))
