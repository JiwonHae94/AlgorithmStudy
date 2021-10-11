# -------------------------------------
# category :
# Q : 이 전화 키패드에서 왼손과 오른손의 엄지손가락만을 이용해서 숫자만을 입력하려고 합니다.
#     맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작하며, 엄지손가락을 사용하는 규칙은 다음과 같습니다.
#     1. 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
#     2. 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
#     3. 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
#     4. 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
#        4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.
# url : https://programmers.co.kr/learn/courses/30/lessons/67256
# 설명 : hashmap
# --------------------------------------
# space complexity : O(n)
# time complexity : O(n)

def solution(numbers, hand):
    answer = ""
    phone = {1: [0, 0, "L"],
             2: [1, 0, "N"],
             3: [2, 0, "R"],
             4: [0, 1, "L"],
             5: [1, 1, "N"],
             6: [2, 1, "R"],
             7: [0, 2, "L"],
             8: [1, 2, "N"],
             9: [2, 2, "R"],
             "*": [0, 3, "L"],
             0: [1, 3, "N"],
             "#": [2, 3, "R"]}

    left_coo = phone["*"][:-1]
    right_coo = phone["#"][:-1]

    for i in numbers:
        num = phone[i]

        if num[-1] == "R":
            answer += num[-1]
            right_coo = num[:-1]

        elif num[-1] == "L":
            answer += num[-1]
            left_coo = num[:-1]

        else:
            dis_from_left = get_distance(left_coo[0], left_coo[1], num[0], num[1])
            dis_from_right = get_distance(right_coo[0], right_coo[1], num[0], num[1])

            if dis_from_left == dis_from_right:
                if hand == "left":
                    answer += "L"
                    left_coo = num[:-1]
                else:
                    answer += "R"
                    right_coo = num[:-1]
            else:
                if dis_from_left < dis_from_right:
                    answer += "L"
                    left_coo = num[:-1]
                else:
                    answer += "R"
                    right_coo = num[:-1]

    return answer


def get_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


# -------------------------------------
# category :
# Q : Finn은 요즘 수학공부에 빠져 있습니다. 수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다.
#     예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.
# url : https://programmers.co.kr/learn/courses/30/lessons/12924
# 설명 : dp
# --------------------------------------
# space complexity : O(n)
# time complexity : O(n)

def solution(n):
    answer = 0
    li = [i + 1 for i in range(n)]

    for i in range(n + 1):
        for j in range(i, n + 1):
            if sum(li[i:j]) == n:
                answer += 1
            elif sum(li[i:j]) > n:
                break

    return answer