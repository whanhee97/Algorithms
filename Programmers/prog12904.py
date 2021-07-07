# 프로그래머스 - 가장 긴 팰린드롬
# https://programmers.co.kr/learn/courses/30/lessons/12904

def solution(s):
    answer = 0
    maxOddCnt = 0
    maxEvenCnt = 0
    for i in range(len(s)):
        oddCnt = 0
        evenCnt = 0
        # 짝수
        if i+1 != len(s) and s[i] == s[i+1]:
            for j in range(1, min(i, len(s)-i-2)+1):
                if s[i+1+j] == s[i-j]:
                    evenCnt += 1
                else:
                    break
        # 홀수
        for j in range(1, min(i, len(s)-i-1)+1):
            if s[i+j] == s[i-j]:
                oddCnt += 1
            else:
                break

        if maxOddCnt <= oddCnt:
            maxOddCnt = oddCnt

        if maxEvenCnt <= evenCnt:
            maxEvenCnt = evenCnt

    if maxEvenCnt == 0 and maxOddCnt == 0:
        return 1
    answer = max(maxOddCnt*2+1, maxEvenCnt*2+2)
    return answer


print(solution("abcde"))


def longest_palindrom(s):
    # 함수를 완성하세요
    s = s.lower()
    results = []

    for i in range(len(s)):
        for j in range(0, i):
            chunk = s[j:i + 1]

            if chunk == chunk[::-1]:
                results.append(chunk)

    return len(max(results, key=len))
