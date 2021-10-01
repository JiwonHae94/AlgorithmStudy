
# -------------------------------------
# category :
# Q : Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고
#     테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.
#
#     Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때
#     카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.
#     url : https://programmers.co.kr/learn/courses/30/lessons/42842
# 설명 : 완전탐색
# --------------------------------------
# space complexity : O(n)
# time complexity : O(1)

def solution(brown, yellow):
    total = brown + yellow

    for i in range(1, total):
        if total % i == 0:
            w = i
            h = int(total / w)

            if (w - 2) * (h - 2) == yellow:
                return [h, w]

    return [1, total]



# -------------------------------------
# category :
# Q :  카카오는 하반기 경력 개발자 공개채용을 진행 중에 있으며 현재 지원서 접수와 코딩테스트가 종료되었습니다. 이번 채용에서 지원자는 지원서 작성 시 아래와 같이 4가지 항목을 반드시 선택하도록 하였습니다.
#      코딩테스트 참여 개발언어 항목에 cpp, java, python 중 하나를 선택해야 합니다.
#      지원 직군 항목에 backend와 frontend 중 하나를 선택해야 합니다.
#      지원 경력구분 항목에 junior와 senior 중 하나를 선택해야 합니다.
#      선호하는 소울푸드로 chicken과 pizza 중 하나를 선택해야 합니다.
#     url : https://programmers.co.kr/learn/courses/30/lessons/72412
# 설명 : dfs, binary_search
# --------------------------------------
# space complexity : O(n * 16)
# time complexity : O(log(n))

from collections import defaultdict
import bisect

def solution(info, query):
    answer = []
    keep = defaultdict(list)

    def create_all_cases(x, index, value):
        if index == 4:
            keep["".join(x)].append(value)
            return

        for i in (True, False):
            if i:
                create_all_cases(x, index + 1, value)
            else:
                t = x.copy()
                t[index] = "-"
                create_all_cases(t, index + 1, value)

    def search_match(candidates, val):
        n = len(candidates)

        return n - bisect.bisect_left(candidates, val, lo=0, hi=n)

    for i in info:
        item = i.split(" ")
        create_all_cases(item[:-1], 0, int(item[-1]))

    for key in keep.keys():
        keep[key].sort()

    for q in query:
        _q = q.split(" ")
        score = int(_q[-1])
        _q = "".join([x for x in _q[:-1] if x != "and"])
        answer.append(search_match(keep[_q], score))

    return answer