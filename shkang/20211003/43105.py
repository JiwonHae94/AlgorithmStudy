"""
위와 같은 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다. 아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다. 예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.

삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.

https://programmers.co.kr/learn/courses/30/lessons/43105
설명: 맨 위의 값을 dp 에 저장해놓고 차례차례 내려가면서 저장해놓은 값을 이용해 더하고 그 더한값들을 다시 저장해놓고 다음 layer에서 다시 사용하면서 더해나감


space complexity : O(triangle)
time complextity : O(triangle^2)

"""


def solution(triangle):

    dp = triangle[0]
    for i in range(len(triangle)-1):
        tmp_dp = []
        prev = None
        for j in range(len(triangle[i])):
            if prev != None:
                if dp[j]+ triangle[i+1][j] > prev:
                    tmp_dp.append(dp[j]+ triangle[i+1][j])
                else:
                    tmp_dp.append(prev)
            else:
                tmp_dp.append(dp[j]+ triangle[i+1][j])
            prev = dp[j]+ triangle[i+1][j+1]

            if j == len(triangle[i])-1:
                tmp_dp.append(dp[j]+ triangle[i+1][j+1])
        dp = tmp_dp

    return max(dp)

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))