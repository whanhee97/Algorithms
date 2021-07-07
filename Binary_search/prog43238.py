# 프로그래머스 이분탐색 - 입국심사
# https://programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    Min = 1
    Max = max(times)*n
    left, right = Min, Max
    answer = right

    while right >= left:
        people = 0  # 심사관이 심사본 사람 수
        mid = (left + right) // 2
        for t in times:
            # 전체시간(mid) 에서 각 심사관이 본 시간을 나누면 각 심사관이 볼 수 있는 사람수가 되므로 이걸 모두 더해줌
            people += (mid//t)

        if people >= n:  # 주어진 n이 심사 볼 수 있는 사람 수가 보다 적거나 같으면 시간을 줄여야 하므로 right를 mid-1로 해서 시간을 줄이는 쪽으로 범위를 좁힌다
            if answer >= mid:  # n이 people 보다 작은 answer중 최솟값을 찾는다
                answer = mid
            right = mid - 1
        else:  # 심사 볼 수  있는 사람이 n보다 적으면 성립이 안되므로 시간을 늘리는 쪽으로 범위를 좁힌다
            left = mid + 1
    return answer


n = 6
times = [7, 10]
print(solution(n, times))
