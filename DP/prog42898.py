def solution(m, n, puddles):
    answer = 0
    dp = [[1 for _ in range(m)] for _ in range(n)]  # 일단 1로 초기화
    for p in puddles:
        if p[1] == n:  # 만약 왼쪽 벽에 웅덩이가 있으면 그 웅덩이 위로도 전부 0으로 바꿔줌
            for i in range(p[0]):
                dp[p[1]-1][i] = 0
        elif p[0] == m:  # 밑에 벽에 웅덩이가 있으면 그 웅덩이 왼쪽으로 전부 0으로 바꿔줌
            for i in range(p[1]):
                dp[i][p[0]-1] = 0
        else:  # 웅덩이면 0으로 표시
            dp[p[1]-1][p[0]-1] = 0

    for i in range(n-2, -1, -1):
        for j in range(m-2, -1, -1):
            if dp[i][j] == 0:  # 현재 위치가 웅덩이면 패스
                continue
            dp[i][j] = dp[i][j+1] + dp[i+1][j]  # 웅덩이가 아니면 오른쪽이랑 밑에 값 더해줌
    # integer의 범위보다 넘어갈 수 있으므로 효율성을 위해 모듈러 연산 해줌
    answer = dp[0][0] % 1000000007
    return answer


m = 4
n = 3
puddles = [[4, 2], [2, 3]]
solution(m, n, puddles)
