# -------------------------------------
# category :
# Q : 첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100)
#     다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)
#     다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다.
#     사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.
#
#     다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)
#     다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데,  정수 X와 문자 C로 이루어져 있으며.
#     게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다.
#     X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.
def solution():
    N = int(input())
    grid = [["#" for i in range(N)] for j in range(N)]
    apples = []
    seconds = 1

    K = int(input())

    for i in range(K):
        apple_coo = list(map(int, input().split()))
        apple_coo[0] -=1
        apple_coo[1] -=1

        apples.append(",".join(map(str, apple_coo)))
        grid[apple_coo[1]-1][apple_coo[0]-1] = "A"

    L = int(input())
    movements = {}

    for mov in range(L):
        mov_ = input().split()
        movements[int(mov_[0]) + 1] = mov_[1]


    dX = [1, -1, 0, 0]
    dY = [0, 0, 1, -1]
    snake = [[0, 0]]
    cur_dir = 0

    while True:

        if seconds in movements:
            cur_dir = rotate_head(cur_dir, movements[seconds])

        headX, headY = snake[0]
        newX = headX + dX[cur_dir]
        newY = headY + dY[cur_dir]

        if 0 <= newX < N and 0 <= newY < N:
            cont_ = move(snake, newX, newY, apples)

            if not cont_:
                return seconds
            plot(snake, N, apples, seconds)
        else:
            return seconds

        seconds += 1


    return seconds


def rotate_head(prev_dir, rotate_cmd):
    if rotate_cmd == "L":
        if prev_dir == 0:
            return 3
        elif prev_dir == 1:
            return 2
        elif prev_dir == 2:
            return 0
        elif prev_dir == 3:
            return 1

    elif rotate_cmd == "D":
        if prev_dir == 0:
            return 2
        elif prev_dir == 1:
            return 3
        elif prev_dir == 2:
            return 1
        elif prev_dir == 3:
            return 0

def plot(snake, N, apples, seconds):
    print("current : ", seconds)
    new_grid = [["=" for i in range(N)] for j in range(N)]

    for apple_coo in apples:
        apple_coo = apple_coo.split(",")
        new_grid[int(apple_coo[1])][int(apple_coo[0])] = "A"

    for i in snake:
        x, y = i
        new_grid[y][x] = "@"

    for g in new_grid:
        print("".join(g))

    print()

def move(snake, newX, newY, apples):
    dummy = snake[0].copy()
    snake_str = [str(s[0]) + "," + str(s[1]) for s in snake]
    met_apples = False
    head_new_pos = str(newX) + "," + str(newY)

    print(snake_str, head_new_pos)

    if head_new_pos in apples:
        apples.remove(str(newX) + "," + str(newY))
        met_apples = True

    if head_new_pos in snake_str :
        return False

    snake[0] = [newX, newY]

    for i in range(1, len(snake)):
        temp = snake[i]
        snake[i] = dummy
        dummy = temp

    if(met_apples):
        snake.append(dummy)

    return True


ans = solution()
print("ans : ", ans)