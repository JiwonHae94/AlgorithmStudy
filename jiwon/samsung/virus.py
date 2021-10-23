# -------------------------------------
# category : Simulation
# Q : 인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다. 다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.
#     연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다.
#     일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.
#     예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자.

#     url : https://www.acmicpc.net/problem/14502
#     설명 : dfs와 combiation을 이용해 경우의 수를 구해 결과물을 도출하는 문제
# --------------------------------------
# space complexity : O(n) -> 추가 메모리 사용 없음
# time complexity : O(n) -> sum(list)할때 루프



from itertools import combinations
import copy

M, N = list(map(int, input().split()))
board = [list(map(str, input().split())) for _ in range(M)]

def solve():
    answer = 0

    for i in get_building_comb():
        temp_board = copy.deepcopy(board)
        put(i, temp_board)
        answer = max(answer, spread_virus(temp_board))

    return answer

def put(pillers, board):
    for i in pillers:
        board[i[0]][i[1]] = "1"

def get_building_comb():
    empty = []

    for i in range(M):
        for j in range(N):
            if board[i][j] == "0":
                empty.append([i, j])

    return combinations(empty, 3)

def spread_virus(b):
    viruses = v.copy()

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while viruses:
        curX, curY = viruses.pop(0)

        for i in range(4):
            newX = dx[i] + curX
            newY = dy[i] + curY

            if 0 <= newX < N and 0 <= newY < M:
                if b[newY][newX] == "0":
                    b[newY][newX] = "2"
                    viruses.append([newX, newY])
    return count_safe_space(b)

def find_virus():
    vi_ = []
    for i in range(M):
        for j in range(N):
            if board[i][j] == "2":
                vi_.append([j, i])
    return vi_


def debug_print_board(b):
    for r in b:
        print(" ".join(r))
    print()

def count_safe_space(b):
    cnt = 0

    for i in range(M):
        for j in range(N):
            if b[i][j] == "0":
                cnt +=1

    return cnt

v = find_virus()
ans = solve()
print(ans)