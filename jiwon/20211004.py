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



# -------------------------------------
# category : Greedy
# Q :  어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.
#      예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다.
#      이 중 가장 큰 숫자는 94 입니다.
#      문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다.
#      number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.
# 설명 : Greedy
# --------------------------------------
# space complexity : O(n)
# time complexity : O(n)
def solution(number, k):
    stack = []

    for i in range(len(number)):
        while k > 0 and stack and int(stack[-1]) < int(number[i]):
            stack.pop()
            k -= 1
        stack.append(number[i])

    if k > 0:
        stack = stack[:-k]

    return "".join(stack)