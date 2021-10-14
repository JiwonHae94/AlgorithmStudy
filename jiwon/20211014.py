# -------------------------------------
# category :
# Q : 게임 캐릭터를 4가지 명령어를 통해 움직이려 합니다. 명령어는 다음과 같습니다.
#     U: 위쪽으로 한 칸 가기
#     D: 아래쪽으로 한 칸 가기
#     R: 오른쪽으로 한 칸 가기
#     L: 왼쪽으로 한 칸 가기
#
#     캐릭터는 좌표평면의 (0, 0) 위치에서 시작합니다. 좌표평면의 경계는 왼쪽 위(-5, 5), 왼쪽 아래(-5, -5), 오른쪽 위(5, 5), 오른쪽 아래(5, -5)로 이루어져 있습니다.
#
# url : https://programmers.co.kr/learn/courses/30/lessons/49994
# 설명 : array
# --------------------------------------
# space complexity : O(n)
# time complexity : O(n)

def solution(dirs):
    direction = {"U": 0, "D": 1, "R": 2, "L": 3}
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    curX, curY = 0, 0
    prev = "0,0"
    path = []

    for i in dirs:
        index = direction[i]

        if -5 <= curX + dx[index] <= 5 and -5 <= curY + dy[index] <= 5:
            curX += dx[index]
            curY += dy[index]

            cur_pos = str(curX) + "," + str(curY)
            _path = prev + "->" + cur_pos
            _path_r = cur_pos + "->" + prev
            prev = cur_pos

            if _path not in path and _path_r not in path:
                path.append(_path)
                path.append(_path_r)

    return len(path) // 2