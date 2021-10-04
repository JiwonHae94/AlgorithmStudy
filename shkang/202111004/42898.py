"""
계속되는 폭우로 일부 지역이 물에 잠겼습니다. 물에 잠기지 않은 지역을 통해 학교를 가려고 합니다. 집에서 학교까지 가는 길은 m x n 크기의 격자모양으로 나타낼 수 있습니다.

아래 그림은 m = 4, n = 3 인 경우입니다.

https://programmers.co.kr/learn/courses/30/lessons/42898

설명: [m+1, n+1] 크기의 matrix를 0으로 초기화 하고 오른쪽, 밑으로 가면서 갈수 있을때 마다 그 좌표의 위, 왼쪽 좌표값을 더해주면서
[m,n]까지 진행해 주면 m,n에는 최종적으로 최단거리로 도착한 애들의 개수가 나온다.


space complexity : O((m+1)*(n+1))
time complextity : O(n*m)

"""

def solution(m, n, puddles):
    dp = [[0] * (m + 1) for i in range(n + 1)]
    dp[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1: continue
            if [j, i] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
    return dp[n][m]

m = 4
n = 3
puddles = [[2, 2]]


print(solution(m, n, puddles))