# 프로그래머스 - 체육복
# https://programmers.co.kr/learn/courses/30/lessons/42862?language=python3

# def solution(n, lost, reserve):
#     answer = 0
#     reserve.sort()
#     lost.sort()
#     cnt = 0
    
    #### 중복제거 과정 
#     x = 0
#     while x < len(lost) :
#         temp = lost[x]
#         if temp in reserve:
#             lost.remove(temp)
#             reserve.remove(temp)
#             continue
#         x += 1
            
          
#     check = [0 for _ in range(len(reserve))]
#     for l in lost:
#         for ir in range(len(reserve)):
#             if check[ir] == 1:
#                 continue
#             if l == reserve[ir] + 1 or l == reserve[ir] - 1 :
#                 cnt += 1
#                 check[ir] = 1
#                 break
    
#     answer = n - len(lost) + cnt
#     return answer
def solution(n, lost, reserve):

    #### 중복제거 과정 
    _reserve = list(set(reserve)-set(lost))
    _lost = list(set(lost)-set(reserve))
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)

n = 5
lost = [2,4,5]
reserve = [3,5]
print(solution(n,lost,reserve))