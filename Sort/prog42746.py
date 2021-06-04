# 프로그래머스 정렬 - 가장 큰 수
# https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    arr = sorted(list(map(str, numbers)), key=lambda x: x*5, reverse=True)
    # ''.join(arr) 원래 여기 까지만 해주면 되나 [0,0,0,0] 들어올시를 대비해
    answer = str(int(''.join(arr)))
    return answer


print(solution([3, 30, 34, 5, 9]))
