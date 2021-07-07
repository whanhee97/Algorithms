# Summer/Winter Coding(~2018) - 점프와 순간 이동
# https://programmers.co.kr/learn/courses/30/lessons/12980

def solution(n):
    ans = 0
    while n != 0:
        if n % 2 == 1:
            n = n//2
            ans += 1
        else:
            n = n/2
    return ans


print(solution(6))
