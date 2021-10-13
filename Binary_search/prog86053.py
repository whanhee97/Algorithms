# 프로그래머스 - 금과 은 운반하기
# https://programmers.co.kr/learn/courses/30/lessons/86053

def solution(a, b, g, s, w, t):
    answer = 4*10**14
    start = 0
    end = 4*10**14
    while end >= start:
        mid = (end + start)//2  # 주어진 시간
        gold = 0  # 주어진 시간 내에 옮길 수 있는 금의 양
        silver = 0  # 주어진 시간 내에 옮길 수 있는 은의 양
        add = 0  # 주어진 시간 내에 옮길 수 있는 (금+은)의 양
        for i in range(len(t)):
            now_g = g[i]
            now_s = s[i]
            now_w = w[i]
            now_t = t[i]
            move_cnt = mid//(now_t*2)  # 운반 횟수 = 주어진 시간을 왕복 걸리는 시간으로 나눔
            if mid % (now_t*2) >= now_t:  # 근데 나머지가 편도 걸리는 시간보다 크면 편도로 한번 더 갈 수 있으므로 운반을 한번 더 할 수 있음
                move_cnt += 1
            # 현재 도시의 금량과 최대로 옮길수 있는 광물의 양을 비교해 작은 쪽을 더해줌
            gold += min(now_g, move_cnt*now_w)
            silver += min(now_s, move_cnt*now_w)
            add += min(now_g+now_s, move_cnt*now_w)
        # 만약에 a보다 주어진 시간내에 옮길 수 있는 금의 양이 많고, b보다 ..., a+b보다 ... 세 가지 조건을 모두 만족하면 시간을 줄여서 최소값을 찾고
        if gold >= a and silver >= b and add >= a+b:
            end = mid - 1
            answer = min(mid, answer)
        else:  # 그렇지 않다면 주어진 시간을 늘려라
            start = mid + 1
    return answer
