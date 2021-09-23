
# ------------------------------------------------------------
# category : 카카오, regex
# Q : 카카오에 입사한 신입 개발자 네오는 "카카오계정개발팀"에 배치되어, 카카오 서비스에 가입하는 유저들의 아이디를 생성하는 업무를 담당하게 되었습니다.
#     "네오"에게 주어진 첫 업무는 새로 가입하는 유저들이 카카오 아이디 규칙에 맞지 않는 아이디를 입력했을 때, 입력된 아이디와 유사하면서 규칙에 맞는 아이디를 추천해주는 프로그램을 개발하는 것입니다.
# ------------------------------------------------------------
# Condition:
# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
# ------------------------------------------------------------

# url : https://programmers.co.kr/learn/courses/30/lessons/72410
# 설명 : regex string match를 통해 조건에 부합하는 캐릭터 찾기

def solution(new_id):
    ans = condition1(new_id)
    ans = condition2(ans)
    ans = condition3(ans)
    ans = condition4(ans)

    #condition 5
    if not ans:
        ans = "a"

    #condition 6_1
    ans = ans[:15]

    #condtiion 6_2
    ans = condition4(ans)

    ans = condition7(ans)
    return ans


def condition1(s):
    return s.lower()


import re

def condition2(s):
    pattern = re.compile("[a-z0-9_\.-]$")
    s = list(s)
    p = 0
    while p < len(s):
        if pattern.match(s[p]):
            p += 1
        else:
            s.pop(p)

    return "".join(s)


def condition3(s):
    s = list(s)
    pointer = 1

    while pointer < len(s):
        if (s[pointer - 1] == s[pointer] == "."):
            s.pop(pointer)
        else:
            pointer += 1

    return "".join(s)


def condition4(s):
    s = list(s)
    while s and s[0] == ".":
        s.pop(0)

    while s and s[-1] == ".":
        s.pop()

    return "".join(s)


def condition7(s):
    s = list(s)
    while len(s) < 3:
        s += s[-1]
    return "".join(s)
