# 프로그래머스 Summer/Winter Coding(2019) - 멀쩡한 사각형
# https://programmers.co.kr/learn/courses/30/lessons/62048
def solution(w, h):
    answer = w*h - (w+h-gcd(w, h))
    return answer


def gcd(x, y):
    r = x % y
    if r == 0:
        return y
    return gcd(y, r)


print(gcd(12, 16))
