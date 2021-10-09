"""
도둑이 어느 마을을 털 계획을 하고 있습니다. 이 마을의 모든 집들은 아래 그림과 같이 동그랗게 배치되어 있습니다.


각 집들은 서로 인접한 집들과 방범장치가 연결되어 있기 때문에 인접한 두 집을 털면 경보가 울립니다.

각 집에 있는 돈이 담긴 배열 money가 주어질 때, 도둑이 훔칠 수 있는 돈의 최댓값을 return 하도록 solution 함수를 작성하세요.


https://programmers.co.kr/learn/courses/30/lessons/42897

설명: 첫번째가 포함될때와 마지막이 포함될때 2가지를 고려해서 시작해서 인접한 집을 털지않으면서 큰 놈들만 더해서 최댓값 return


space complexity : O(money)
time complextity : O(money)

"""
from collections import defaultdict

def solution(money):


    dp1 = defaultdict()
    dp1[0] = 0
    dp1[1] = money[0]

    dp2 = defaultdict()
    dp2[0] = 0
    dp2[1] = 0

    for i in range(2, len(money) + 1):
        if i < len(money):
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i - 1])
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i - 1])
        elif i == len(money):
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i - 1])

    answer = max(dp1[len(money)-1], dp2[len(money)])
    return answer

money = [1, 2, 3, 1]

print(solution(money))