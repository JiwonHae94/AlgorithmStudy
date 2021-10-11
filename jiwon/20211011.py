# -------------------------------------
# category :
# Q : △△ 게임대회가 개최되었습니다. 이 대회는 N명이 참가하고, 토너먼트 형식으로 진행됩니다. N명의 참가자는 각각 1부터 N번을 차례대로 배정받습니다.
#     그리고, 1번↔2번, 3번↔4번, ... , N-1번↔N번의 참가자끼리 게임을 진행합니다.
#     각 게임에서 이긴 사람은 다음 라운드에 진출할 수 있습니다. 이때, 다음 라운드에 진출할 참가자의 번호는 다시 1번부터 N/2번을 차례대로 배정받습니다.
#     만약 1번↔2번 끼리 겨루는 게임에서 2번이 승리했다면 다음 라운드에서 1번을 부여받고, 3번↔4번에서 겨루는 게임에서 3번이 승리했다면 다음 라운드에서 2번을 부여받게 됩니다.
#     게임은 최종 한 명이 남을 때까지 진행됩니다.
#     이때, 처음 라운드에서 A번을 가진 참가자는 경쟁자로 생각하는 B번 참가자와 몇 번째 라운드에서 만나는지 궁금해졌습니다.
#     게임 참가자 수 N, 참가자 번호 A, 경쟁자 번호 B가 함수 solution의 매개변수로 주어질 때,
#     처음 라운드에서 A번을 가진 참가자는 경쟁자로 생각하는 B번 참가자와 몇 번째 라운드에서 만나는지 return 하는 solution 함수를 완성해 주세요.
#     단, A번 참가자와 B번 참가자는 서로 붙게 되기 전까지 항상 이긴다고 가정합니다.
#     즉, 이 경우가 최소가 되므로 29를 return 합니다.
#     배열 A, B가 주어질 때 최종적으로 누적된 최솟값을 return 하는 solution 함수를 완성해 주세요.
# url : https://programmers.co.kr/learn/courses/30/lessons/12941
# 설명 : hashmap
# --------------------------------------
# space complexity : O(n)
# time complexity : O(n)
def solution(n, a, b):
    num_round = 1
    index_A = a
    index_B = b

    while True:
        if abs(index_A - index_B) == 1 and (index_A % 2 + index_A // 2 == index_B // 2 + index_B % 2):
            break

        index_A = (index_A + int(index_A % 2)) // 2
        index_B = (index_B + int(index_B % 2)) // 2
        num_round += 1

    return num_round