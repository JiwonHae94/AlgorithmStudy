# -------------------------------------
# category :
# Q : 프렌즈4블록
#     블라인드 공채를 통과한 신입 사원 라이언은 신규 게임 개발 업무를 맡게 되었다. 이번에 출시할 게임 제목은 "프렌즈4블록".
#     같은 모양의 카카오프렌즈 블록이 2×2 형태로 4개가 붙어있을 경우 사라지면서 점수를 얻는 게임이다.
#     board map
#     만약 판이 위와 같이 주어질 경우, 라이언이 2×2로 배치된 7개 블록과 콘이 2×2로 배치된 4개 블록이 지워진다. 같은 블록은 여러 2×2에 포함될 수 있으며, 지워지는 조건에 만족하는 2×2 모양이 여러 개 있다면 한꺼번에 지워진다.
#     board map
#     블록이 지워진 후에 위에 있는 블록이 아래로 떨어져 빈 공간을 채우게 된다.
#     board map
#     만약 빈 공간을 채운 후에 다시 2×2 형태로 같은 모양의 블록이 모이면 다시 지워지고 떨어지고를 반복하게 된다.
#     board map
#     위 초기 배치를 문자로 표시하면 아래와 같다. 위 예의 경우, 1행의 네번째 칸 (5), 2행의 세번째 칸 (7), 3행의 첫번째 칸 (4) 땅을 밟아 16점이 최고점이 되므로 16을 return 하면 됩니다.
#
#     TTTANT
#     RRFACC
#     RRRFCC
#     TRRRAA
#     TTMMMF
#     TMMTTJ
#
#     각 문자는 라이언(R), 무지(M), 어피치(A), 프로도(F), 네오(N), 튜브(T), 제이지(J), 콘(C)을 의미한다
#     입력으로 블록의 첫 배치가 주어졌을 때, 지워지는 블록은 모두 몇 개인지 판단하는 프로그램을 제작하라.
# url : https://programmers.co.kr/learn/courses/30/lessons/17679
# 설명 : array
# --------------------------------------
# space complexity : O(n^3)
# time complexity : O(n^3)
def solution(m, n, board):
    answer = 0

    board = init_board(board)
    board_updated = True

    while board_updated:
        pop_blocks = set()

        for y in range(m):
            for x in range(n):
                pop_ = check_four_block(board, x, y)
                if pop_:
                    pop_blocks.update(pop_)

        board_updated = len(pop_blocks) > 0
        update_board(board, pop_blocks)
        answer += len(pop_blocks)

    return answer


def init_board(board):
    return [[item for item in row] for row in board]


def update_board(board, pop_items):
    if len(pop_items) < 1:
        return
    width, height = len(board[0]), len(board)

    for items in pop_items:
        x, y = map(int, items.split(","))
        board[y][x] = " "

    for c in range(1, height):
        for r in range(width):
            if board[c][r] == " ":
                for i in range(0, c):
                    board[c - i][r] = board[c - i - 1][r]
                    board[c - i - 1][r] = " "


def check_four_block(board, x, y):
    start_block = board[y][x]
    dx = [x + 1, x + 0, x + 1]
    dy = [y + 0, y + 1, y + 1]
    width, height = len(board[0]), len(board)

    all_blocks = [start_block]

    for i in range(3):
        if 0 <= dx[i] < width and 0 <= dy[i] < height:
            all_blocks.append(board[dy[i]][dx[i]])

    if len(all_blocks) == 4 and len(set(all_blocks)) == 1 and not " " in all_blocks:
        return [str(x) + "," + str(y)] + [str(dx[i]) + "," + str(dy[i]) for i in range(3)]
    else:
        return None

