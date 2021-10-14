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


# -------------------------------------
# category :
# Q : 선행 스킬이란 어떤 스킬을 배우기 전에 먼저 배워야 하는 스킬을 뜻합니다.
#     예를 들어 선행 스킬 순서가 스파크 → 라이트닝 볼트 → 썬더일때, 썬더를 배우려면 먼저 라이트닝 볼트를 배워야 하고, 라이트닝 볼트를 배우려면 먼저 스파크를 배워야 합니다.
#     위 순서에 없는 다른 스킬(힐링 등)은 순서에 상관없이 배울 수 있습니다. 따라서 스파크 → 힐링 → 라이트닝 볼트 → 썬더와 같은 스킬트리는 가능하지만, 썬더 → 스파크나 라이트닝 볼트 → 스파크 → 힐링 → 썬더와 같은 스킬트리는 불가능합니다.
#     선행 스킬 순서 skill과 유저들이 만든 스킬트리1를 담은 배열 skill_trees가 매개변수로 주어질 때, 가능한 스킬트리 개수를 return 하는 solution 함수를 작성해주세요.
#
#     제한 조건
#     스킬은 알파벳 대문자로 표기하며, 모든 문자열은 알파벳 대문자로만 이루어져 있습니다.
#     스킬 순서와 스킬트리는 문자열로 표기합니다.
#     예를 들어, C → B → D 라면 "CBD"로 표기합니다
#     선행 스킬 순서 skill의 길이는 1 이상 26 이하이며, 스킬은 중복해 주어지지 않습니다.
#     skill_trees는 길이 1 이상 20 이하인 배열입니다.
#     skill_trees의 원소는 스킬을 나타내는 문자열입니다.
#     skill_trees의 원소는 길이가 2 이상 26 이하인 문자열이며, 스킬이 중복해 주어지지 않습니다
# url : https://programmers.co.kr/learn/courses/30/lessons/49993
# 설명 : hashmap, list
# --------------------------------------
# space complexity : O(n)
# time complexity : O(n)
def solution(skill, skill_trees):
    answer = 0
    skill_repo = {skill[0]: None}

    for i in range(1, len(skill)):
        skill_repo[skill[i]] = skill[i - 1]

    for s in skill_trees:
        learned_ = []
        _is_valid = True

        for item in s:

            if item in skill_repo:
                if not skill_repo[item] or skill_repo[item] in learned_:
                    learned_.append(item)
                else:
                    _is_valid = False
                    break

        answer += int(_is_valid)

    return answer
