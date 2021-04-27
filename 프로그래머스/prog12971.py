# Summer/Winter Coding(~2018) - 스티커 모으기(2)
# https://programmers.co.kr/learn/courses/30/lessons/12971

def solution(sticker):
    answer = 0
    if len(sticker) == 1:
        return sticker[0]
    dp1 = [0 for _ in range(len(sticker))]  # dp1은 첫번째를 쓸때
    dp2 = [0 for _ in range(len(sticker))]  # dp2은 첫번째를 안 쓸때
    dp1[0], dp1[1] = sticker[0], sticker[0]  # 첫번째를 쓰므로 두번째도 첫번째랑 같음
    dp2[0], dp2[1] = 0, sticker[1]  # 첫번째를 안 쓰므로 맨처음은 0 이고 두번째 부터 시작
    for i in range(2, len(sticker)-1):  # 첫번째를 쓰면 맨 마지막을 제외하고 dp계산
        # 스티커의 i번째 쓸때와 안 쓸때중 큰값을 저장
        dp1[i] = max(dp1[i-2]+sticker[i], dp1[i-1])
    for i in range(2, len(sticker)):  # 안 쓰면 맨 마지막 까지 계산
        dp2[i] = max(dp2[i-2]+sticker[i], dp2[i-1])

    answer = max(max(dp1), max(dp2))
    return answer


sticker = [1]
print(solution(sticker))
