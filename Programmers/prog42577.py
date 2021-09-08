# 프로그래머스 - 전화번호 목록
# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution2(phone_book):
    answer = True
    s_pb = sorted(phone_book, key=lambda x: len(x))
    for i in range(len(s_pb)):
        for j in range(i+1, len(s_pb)):
            if s_pb[i] == s_pb[j][:len(s_pb[i])]:
                return False
    return answer


def solution(phone_book):
    answer = True
    s_pb = sorted(phone_book)
    for i in range(len(s_pb)-1):
        if s_pb[i] == s_pb[i+1][:len(s_pb[i])]:
            return False
    return answer


print(solution(["119", "97674223", "1195524421"]))
