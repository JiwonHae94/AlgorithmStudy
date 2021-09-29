

"""
https://programmers.co.kr/learn/courses/30/lessons/43105
위와 같은 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다. 아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다. 예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.

삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.

제한사항
삼각형의 높이는 1 이상 500 이하입니다.
삼각형을 이루고 있는 숫자는 0 이상 9,999 이하의 정수입니다.

Dynamic Programming 문제

"""


def solution1(triangle):
    for i in range(1, len(triangle)):
        for j in range(0, i+1):
            len_num = len(triangle[i][:])
            if j ==0 :  #첫번째는 하나밖에없으니 예외처리
                triangle[i][j] = triangle[i][j] + (triangle[i - 1][j])
            elif j == len_num-1: #맨끝도 마찬가지
                triangle[i][j] = triangle[i][j] + (triangle[i - 1][j-1])
            else: #가운데는 양쪽꺼중 큰거
                triangle[i][j] = triangle[i][j] + max(triangle[i-1][j-1], triangle[i-1][j])

    return max(triangle[-1]) #가장 마지막에서 젤큰거



def solution2(triangle):
    triangle = [[0] + line + [0]  for line in triangle] #예외처리 귀찮으니까 걍 양쪽에 0 붙여버리자 어차피 0은 더해도 영향 안줌
    for i in range(1, len(triangle)):
        for j in range(0, i+2):
            triangle[i][j] = triangle[i][j] + max(triangle[i-1][j-1], triangle[i-1][j])
    return max(triangle[-1]) #가장 마지막에서 젤큰거


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution1(triangle))
print(solution2(triangle))