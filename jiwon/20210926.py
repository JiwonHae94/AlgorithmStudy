
# -------------------------------------
# category :
# Q : 카카오에 신입 개발자로 입사한 "콘"은 선배 개발자로부터 개발역량 강화를 위해 다른 개발자가 작성한 소스 코드를 분석하여 문제점을 발견하고 수정하라는 업무 과제를 받았습니다.
#     소스를 컴파일하여 로그를 보니 대부분 소스 코드 내 작성된 괄호가 개수는 맞지만 짝이 맞지 않은 형태로 작성되어 오류가 나는 것을 알게 되었습니다.
#     수정해야 할 소스 파일이 너무 많아서 고민하던 "콘"은 소스 코드에 작성된 모든 괄호를 뽑아서 올바른 순서대로 배치된 괄호 문자열을 알려주는 프로그램을 다음과 같이 개발하려고 합니다.
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