# 프로그래머스 - 조이스틱
# https://programmers.co.kr/learn/courses/30/lessons/42860

# 그리디 문제 - 핵심은 양 옆으로 무빙하는 개수. 현재 인덱스로부터 오른쪽 왼쪽을 비교해 A가 아닌 곳에 가까운 쪽으로 이동함. 거기를 A로 만들고 다시 똑같이 반복
def solution(name):
    answer = 0
    name = list(name)
    upDown = []
    for i in name:
        upDown.append(min(ord(i)-ord('A'), ord('Z')-ord(i)+1)) #name의 각 자리에 up down 수를 구해서 적어놓음(+1 해주는 이유는 첨 상태에서 왼쪽으로 가는 횟수 추가)
    idx = 0
    while True:
        answer += upDown[idx] # 인덱스에 해당하는 숫자 더해주고
        upDown[idx] = 0 # 그 자리 0으로 만듬
        if sum(upDown) == 0: # 모든 자리 합이 0이 되면 종료
            break
        right = 1 # 한 칸씩 이동하는 것은 고정
        left = 1
        while upDown[idx+right] == 0: # 오른쪽으로 이동한게 0이면 오른쪽으로 한 칸 이동 -> A가 아닌 것 까지의 거리를 오른쪽으로 잰다
            right += 1
        while upDown[idx-left] == 0: # 왼쪽으로 이동한게 0이면 왼쪽으로 한 칸 이동 -> A가 아닌 것 까지의 거리를 왼쪽으로 잰다
            left += 1
        if right <= left: # 더 작은 쪽으로 이동함
            answer += right # 이동한 거리 추가
            idx += right # idx 실제 이동
        else:
            answer += left # 이동한 거리 추가
            idx -= left # idx 실제 이동
    return answer

print(solution("JAN"))