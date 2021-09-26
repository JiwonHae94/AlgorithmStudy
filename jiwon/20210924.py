
# -------------------------------------
# category :
# Q : n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다.
#
# url : https://programmers.co.kr/learn/courses/30/lessons/43165
# 설명 : dfs 를 통해 모든 조합 탐색
# --------------------------------------
# space complexity : 0 -> 추가 메모리 사용 없음
# time complexity : O(n) -> sum(list)할때 루프

def solution(numbers, target):
    return dfs([], numbers, target, len(numbers))

def dfs(temp, numbers, target, k):
    answer = 0

    if len(temp) == k:
        return int(sum(temp) == target)

    answer += dfs(temp + [numbers[0]], numbers[1:], target, k)
    answer += dfs(temp + [-numbers[0]], numbers[1:], target, k)
    return answer

print("ans : ", solution([1, 1, 1, 1, 1], 3))