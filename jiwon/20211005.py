# -------------------------------------
# category :
# Q : JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다.
#     문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수,
#     solution을 완성해주세요.
# url : https://programmers.co.kr/learn/courses/30/lessons/12951
# 설명 : re, python
# --------------------------------------
# space complexity : O(n)
# time complexity : O(n)
def solution(s):
    words = s.lower().split(' ')

    for i in range(len(words)):
        words[i] = words[i].capitalize()

    return " ".join(words)