
# -------------------------------------
# category :
# Q : 개발자를 희망하는 죠르디가 카카오에 면접을 보러 왔습니다.
#     코로나 바이러스 감염 예방을 위해 응시자들은 거리를 둬서 대기를 해야하는데 개발 직군 면접인 만큼
#     아래와 같은 규칙으로 대기실에 거리를 두고 앉도록 안내하고 있습니다.
#     대기실은 5개이며, 각 대기실은 5x5 크기입니다.
#     거리두기를 위하여 응시자들 끼리는 맨해튼 거리1가 2 이하로 앉지 말아 주세요.
#     단 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우에는 허용합니다.
# url : https://programmers.co.kr/learn/courses/30/lessons/42626
# 설명 : Heap
# --------------------------------------
# space complexity : 0 -> 추가 메모리 사용 없음
# time complexity : O(1) -> sum(list)할때 루프

import heapq as hq

def solution(scoville, K):
    answer = 0

    hq.heapify(scoville)

    while True:
        first = hq.heappop(scoville)

        if first >= K:
            return answer
        elif len(scoville) == 0:
            return -1
        else:
            second = hq.heappop(scoville)
            hq.heappush(scoville, first + second * 2)
            answer += 1
