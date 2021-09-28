
# ------------------------------------------------------------
# category : DP
# Q : 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다. 아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다. 예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.

# 삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.


# url : https://programmers.co.kr/learn/courses/30/lessons/43105
# 설명 : triangle 에 맞춰서 정답을 저장(updated value)할 triangle 을 만들어 진행
# time complexity : O(1) ..? triangle 크기가 500 이하라 최대 500 * 500 .. O(500*500) -> O(1) 같음.
# space complexity : IDK 


def solution(triangle):
    import copy
    
    val = copy.deepcopy(triangle)
    
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if i == j:
                val[i][j] = val[i-1][j-1] + triangle[i][j]
            elif j == 0:
                val[i][j] = val[i-1][j] + triangle[i][j]
            else:
                val_left = val[i-1][j-1] + triangle[i][j]
                val_right = val[i-1][j] + triangle[i][j]
                val[i][j] = max(val_left, val_right)
                
    return max(val[len(triangle)-1])
