# -------------------------------------
# category :
# Q :  뉴스 클러스터링
#      여러 언론사에서 쏟아지는 뉴스, 특히 속보성 뉴스를 보면 비슷비슷한 제목의 기사가 많아 정작 필요한 기사를 찾기가 어렵다. Daum 뉴스의 개발 업무를 맡게 된 신입사원 튜브는 사용자들이 편리하게 다양한 뉴스를 찾아볼 수 있도록 문제점을 개선하는 업무를 맡게 되었다.
#      개발의 방향을 잡기 위해 튜브는 우선 최근 화제가 되고 있는 "카카오 신입 개발자 공채" 관련 기사를 검색해보았다.
#      url : https://programmers.co.kr/learn/courses/30/lessons/17677
# 설명 : DP
# --------------------------------------
# space complexity : O(n)
# time complexity : O(n)
import re

def solution(str1, str2):
    def jaccard(s1, s2):
        if not s1 and not s2:
            return 1

        inter = get_intersection(s1, s2)
        union = s1 + s2

        return len(inter) / len(union)

    def get_intersection(s1, s2):
        common = []

        for i in s1:
            if i in s2:
                s2.remove(i)
                common.append(i)

        return common

    def split_two(s):
        pattern = re.compile("[a-zA-Z]{2}")
        index = 0
        substring = []

        while index < len(s) - 1:
            candidate = s[index:index + 2]

            if pattern.match(candidate):
                substring.append(candidate)
            index += 1
        return substring

    s1, s2 = split_two(str1.lower()), split_two(str2.lower())
    return int(jaccard(s1, s2) * 65536)
