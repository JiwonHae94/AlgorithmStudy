import heapq

#
# heapq's default is min heap

# -------------------------------------
# category : Heap
#   매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.
#
#   섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
#   Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
#   Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.


#
#     url : https://programmers.co.kr/learn/courses/30/lessons/42626
#     설명 : heapq 을 이용한 풀이
# --------------------------------------
# space complexity : O(logn) -> heapq is binary heap
# time complexity : O(logn) -> binary heap 이기 때문에 logn 의 시간복잡도를 가짐.


def make_heap(scoville):
    heap = []

    for sco in scoville:
        heapq.heappush(heap, sco)

    return heap

def solution(scoville, K):
    answer = 0
    heap = make_heap(scoville)

    cnt = 0
    while heap[0] < K:
        mix_val = heapq.heappop(heap) + heapq.heappop(heap) * 2
        heapq.heappush(heap, mix_val)

        if len(heap) == 1 and heap[0] < K:
            return -1

        answer += 1

    return answer



