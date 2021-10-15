# -------------------------------------
# category :
# Q : 레스토랑을 운영하던 스카피는 코로나19로 인한 불경기를 극복하고자 메뉴를 새로 구성하려고 고민하고 있습니다.
#     기존에는 단품으로만 제공하던 메뉴를 조합해서 코스요리 형태로 재구성해서 새로운 메뉴를 제공하기로 결정했습니다. 어떤 단품메뉴들을 조합해서 코스요리 메뉴로 구성하면 좋을 지 고민하던 "스카피"는 이전에 각 손님들이 주문할 때 가장 많이 함께 주문한 단품메뉴들을 코스요리 메뉴로 구성하기로 했습니다.
#     단, 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성하려고 합니다. 또한, 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함하기로 했습니다.
#     예를 들어, 손님 6명이 주문한 단품메뉴들의 조합이 다음과 같다면,
#     (각 손님은 단품메뉴를 2개 이상 주문해야 하며, 각 단품메뉴는 A ~ Z의 알파벳 대문자로 표기합니다.)
#     손님 번호	주문한 단품메뉴 조합
#     1번 손님	A, B, C, F, G
#     2번 손님	A, C
#     3번 손님	C, D, E
#     4번 손님	A, C, D, E
#     5번 손님	B, C, F, G
#     6번 손님	A, C, D, E, H
#     가장 많이 함께 주문된 단품메뉴 조합에 따라 "스카피"가 만들게 될 코스요리 메뉴 구성 후보는 다음과 같습니다.
#     코스 종류	메뉴 구성	설명
#     요리 2개 코스	A, C	1번, 2번, 4번, 6번 손님으로부터 총 4번 주문됐습니다.
#     요리 3개 코스	C, D, E	3번, 4번, 6번 손님으로부터 총 3번 주문됐습니다.
#     요리 4개 코스	B, C, F, G	1번, 5번 손님으로부터 총 2번 주문됐습니다.
#     요리 4개 코스	A, C, D, E	4번, 6번 손님으로부터 총 2번 주문됐습니다.
#
# url : https://programmers.co.kr/learn/courses/30/lessons/72411
# 설명 : combinations
# --------------------------------------
# space complexity : O(n)
# time complexity : O(n)
from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []

    for num_food in course:
        menu_counter = defaultdict(int)

        for order in orders:
            menu = list(map(list, combinations(order, num_food)))

            for candidate_menu in menu:
                menu_counter["".join(sorted(candidate_menu))] += 1

        answer += [key for key, value in menu_counter.items() if value == max(menu_counter.values()) and value > 1]

    answer.sort()
    return answer


# -------------------------------------
# category :
# Q : 카카오에 신입 개발자로 입사한 "콘"은 선배 개발자로부터 개발역량 강화를 위해 다른 개발자가 작성한 소스 코드를 분석하여 문제점을 발견하고 수정하라는 업무 과제를 받았습니다. 소스를 컴파일하여 로그를 보니 대부분 소스 코드 내 작성된 괄호가 개수는 맞지만 짝이 맞지 않은 형태로 작성되어 오류가 나는 것을 알게 되었습니다.
#     수정해야 할 소스 파일이 너무 많아서 고민하던 "콘"은 소스 코드에 작성된 모든 괄호를 뽑아서 올바른 순서대로 배치된 괄호 문자열을 알려주는 프로그램을 다음과 같이 개발하려고 합니다.
#     용어의 정의
#     '(' 와 ')' 로만 이루어진 문자열이 있을 경우, '(' 의 개수와 ')' 의 개수가 같다면 이를 균형잡힌 괄호 문자열이라고 부릅니다.
#     그리고 여기에 '('와 ')'의 괄호의 짝도 모두 맞을 경우에는 이를 올바른 괄호 문자열이라고 부릅니다.
#     예를 들어, "(()))("와 같은 문자열은 "균형잡힌 괄호 문자열" 이지만 "올바른 괄호 문자열"은 아닙니다.
#     반면에 "(())()"와 같은 문자열은 "균형잡힌 괄호 문자열" 이면서 동시에 "올바른 괄호 문자열" 입니다.
#     '(' 와 ')' 로만 이루어진 문자열 w가 "균형잡힌 괄호 문자열" 이라면 다음과 같은 과정을 통해 "올바른 괄호 문자열"로 변환할 수 있습니다.
#     1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
#     2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
#     3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
#        3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
#     4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
#        4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
#        4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
#        4-3. ')'를 다시 붙입니다.
#        4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
#        4-5. 생성된 문자열을 반환합니다.
#
# url : https://programmers.co.kr/learn/courses/30/lessons/60058
# 설명 : recursion
# --------------------------------------
# space complexity : O(n)
# time complexity : O(n)
from collections import Counter

def solution(p):
    return helper(p)


def helper(b):
    if not b:
        return ""

    u, v = split(b)

    if is_bracket_valid(u):
        u += helper(v)
        return u
    else:
        s = "(" + helper(v) + ")"
        s += reverse(u[1:-1])
        return s


def split(b):
    left, right = 0, 1
    is_balanced = False

    while right < len(b) and not is_balanced:
        is_balanced = is_bracket_balanced(b[left:right])

        if (is_balanced):
            break
        right += 1

    u, v = b[left:right], b[right:]
    return u, v


def is_bracket_valid(p):
    stack = []

    for i in p:
        if not stack:
            stack.append(i)
        else:
            if i == "(":
                stack.append(i)
            else:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(i)

    return len(stack) == 0


def is_bracket_balanced(p):
    balance_counter = Counter(p)
    return balance_counter["("] == balance_counter[")"]


def reverse(p):
    map = {"(": ")", ")": "("}
    p = list(p)

    for i in range(len(p)):
        p[i] = map[p[i]]

    return "".join(p)


