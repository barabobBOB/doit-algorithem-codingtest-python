def solution(triangle):
    # dp 배열을 삼각형과 동일한 구조로 초기화
    dp = [[0 for _ in range(len(row))] for row in triangle]

    # 가장 아래층에 대한 초기 값 설정
    dp[-1] = triangle[-1]

    # 역순으로 각 층을 순회하며 최대 합 계산
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            dp[i][j] = triangle[i][j] + max(dp[i+1][j], dp[i+1][j+1])
    
    # 삼각형 꼭대기에서 시작하는 최대 합 반환
    return dp[0][0]