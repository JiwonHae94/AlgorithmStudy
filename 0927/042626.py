import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while(True):
        if scoville[0] >=K:
            return answer
        elif len(scoville) == 1:
            return -1
        else :
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            c = a+b*2
            heapq.heappush(scoville,c)
            answer +=1

    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville,K))