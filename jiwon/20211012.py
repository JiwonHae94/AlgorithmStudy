# -------------------------------------
# category :
# Q : 땅따먹기 게임을 하려고 합니다. 땅따먹기 게임의 땅(land)은 총 N행 4열로 이루어져 있고, 모든 칸에는 점수가 쓰여 있습니다.
#     1행부터 땅을 밟으며 한 행씩 내려올 때,
#     각 행의 4칸 중 한 칸만 밟으면서 내려와야 합니다. 단, 땅따먹기 게임에는 한 행씩 내려올 때,
#     같은 열을 연속해서 밟을 수 없는 특수 규칙이 있습니다.
#     예를 들면,
#     | 1 | 2 | 3 | 5 |
#     | 5 | 6 | 7 | 8 |
#     | 4 | 3 | 2 | 1 |
#     로 땅이 주어졌다면, 1행에서 네번째 칸 (5)를 밟았으면, 2행의 네번째 칸 (8)은 밟을 수 없습니다.
#    마지막 행까지 모두 내려왔을 때, 얻을 수 있는 점수의 최대값을 return하는 solution 함수를 완성해 주세요. 위 예의 경우, 1행의 네번째 칸 (5), 2행의 세번째 칸 (7), 3행의 첫번째 칸 (4) 땅을 밟아 16점이 최고점이 되므로 16을 return 하면 됩니다.

# url : https://programmers.co.kr/learn/courses/30/lessons/12913
# 설명 : dp
# --------------------------------------
# space complexity : O(n^2)
# time complexity : O(n^2)

def solution(land):
    for i in range(1, len(land)):
        land[i][0] += max(land[i - 1][1], land[i - 1][2], land[i - 1][3])
        land[i][1] += max(land[i - 1][0], land[i - 1][2], land[i - 1][3])
        land[i][2] += max(land[i - 1][0], land[i - 1][1], land[i - 1][3])
        land[i][3] += max(land[i - 1][0], land[i - 1][1], land[i - 1][2])

    return max(land[-1])

# -------------------------------------
# category :
# Q : N개의 마을로 이루어진 나라가 있습니다.
#    이 나라의 각 마을에는 1부터 N까지의 번호가 각각 하나씩 부여되어 있습니다. 각 마을은 양방향으로 통행할 수 있는 도로로 연결되어 있는데,
#    서로 다른 마을 간에 이동할 때는 이 도로를 지나야 합니다. 도로를 지날 때 걸리는 시간은 도로별로 다릅니다. 현재 1번 마을에 있는 음식점에서 각 마을로 음식 배달을 하려고 합니다.
#    각 마을로부터 음식 주문을 받으려고 하는데, N개의 마을 중에서 K 시간 이하로 배달이 가능한 마을에서만 주문을 받으려고 합니다. 다음은 N = 5, K = 3인 경우의 예시입니다.
#
#    배달_1_uxun8t.png
#
#    위 그림에서 1번 마을에 있는 음식점은 [1, 2, 4, 5] 번 마을까지는 3 이하의 시간에 배달할 수 있습니다.
#    그러나 3번 마을까지는 3시간 이내로 배달할 수 있는 경로가 없으므로 3번 마을에서는 주문을 받지 않습니다.
#    따라서 1번 마을에 있는 음식점이 배달 주문을 받을 수 있는 마을은 4개가 됩니다.
#    마을의 개수 N, 각 마을을 연결하는 도로의 정보 road, 음식 배달이 가능한 시간 K가 매개변수로 주어질 때,
#    음식 주문을 받을 수 있는 마을의 개수를 return 하도록 solution 함수를 완성해주세요.

# url : https://programmers.co.kr/learn/courses/30/lessons/12978
# 설명 : floyd marshall
# --------------------------------------
# space complexity : O(n^3)
# time complexity : O(n^3)
def solution(N, road, K):
    road_map = [[float('inf') for i in range(N)] for j in range(N)]

    for r in road:
        from_, to_, distance = r
        road_map[from_ - 1][to_ - 1] = min(road_map[from_ - 1][to_ - 1], distance)
        road_map[to_ - 1][from_ - 1] = min(road_map[to_ - 1][from_ - 1], distance)

    for i in range(N):
        for j in range(N):
            for k in range(N):
                if road_map[j][i] != float('inf') and road_map[i][k] != float('inf'):
                    road_map[j][k] = min(road_map[j][k], road_map[j][i] + road_map[i][k])

    deliverable = [1]

    for i in range(N):
        if road_map[0][i] <= K:
            deliverable += [i + 1]

    return len(set(deliverable))
