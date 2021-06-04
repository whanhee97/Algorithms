# 프로그래머스 동적계획법 - N으로 표현
# https://programmers.co.kr/learn/courses/30/lessons/42895

def solution(N, number):
    answer = -1
    if number == N:
        return 1
    s = [set() for _ in range(8)]  # s[n] 은 n+1개로 만들 수 있는 수의 집합
    for i in range(8):
        temp = int(str(N)*(i+1))
        s[i].add(temp)

    for i in range(1, 8):  # i는 1~7 까지 순회 -> 계산된 수를 집어 넣을 인덱스
        for j in range(i):  # j는 i 만큼 순회
            for x1 in s[j]:  # j+1개로 만들수 있는 조합들을 하나씩 꺼냄
                # i-j-1 -> i(들어갈 인덱스) - j(x1의 인덱스) -1(인덱스가 0부터 시작하므로)
                for x2 in s[i-j-1]:
                    s[i].add(x1 + x2)
                    s[i].add(x1 - x2)
                    s[i].add(x1 * x2)
                    if x2 != 0:
                        s[i].add(x1 // x2)
        if number in s[i]:
            return i+1
    return answer


N = 2
number = 2
print(solution(N, number))
