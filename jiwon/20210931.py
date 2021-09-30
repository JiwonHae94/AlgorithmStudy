
# -------------------------------------
# category :
# Q : 일반적인 프린터는 인쇄 요청이 들어온 순서대로 인쇄합니다. 그렇기 때문에 중요한 문서가 나중에 인쇄될 수 있습니다.
#     이런 문제를 보완하기 위해 중요도가 높은 문서를 먼저 인쇄하는 프린터를 개발했습니다.
#     이 새롭게 개발한 프린터는 아래와 같은 방식으로 인쇄 작업을 수행합니다.
# url : https://programmers.co.kr/learn/courses/30/lessons/42587
# 설명 : Stack
# --------------------------------------
# space complexity : O(n) -> 추가 메모리 사용 없음
# time complexity : O(2n) -> O(n)

def solution(priorities, location):
    stack = []

    for index, p in enumerate(priorities):
        stack.append([index, p])

    pos = 0
    while stack:
        current = stack.pop(0)

        if len([i for i in stack if i[1] > current[1]]) > 0:
            stack.append(current)
        else:
            pos += 1
            if location == current[0]:
                return pos
    return pos




# -------------------------------------
# category :
# Q : 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#     예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.
#     0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.
#
# url : https://programmers.co.kr/learn/courses/30/lessons/42587
# 설명 : Stack
# --------------------------------------
# space complexity : O(n) -> 추가 메모리 사용 없음
# time complexity : O(2n) -> O(n)

import functools

def compare(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    num_str = [str(x) for x in numbers]
    num_str = sorted(num_str, key=functools.cmp_to_key(compare),reverse=True)
    answer = str(int(''.join(num_str)))
    return answer


# -------------------------------------
# category :
# Q : 1부터 n까지 번호가 붙어있는 n명의 사람이 영어 끝말잇기를 하고 있습니다. 영어 끝말잇기는 다음과 같은 규칙으로 진행됩니다.
#     1번부터 번호 순서대로 한 사람씩 차례대로 단어를 말합니다.
#     마지막 사람이 단어를 말한 다음에는 다시 1번부터 시작합니다.
#     앞사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야 합니다.
#     이전에 등장했던 단어는 사용할 수 없습니다.
#     한 글자인 단어는 인정되지 않습니다.
#     url : https://programmers.co.kr/learn/courses/30/lessons/12981
# 설명 : Stack
# --------------------------------------
# space complexity : O(n)
# time complexity : O(n) -> O(n)

def solution(n, words):
    person, order = 1, 1
    queue = []

    for index, word in enumerate(words):
        if not queue:
            queue.append(word)
            person += 1
        else:
            if word not in queue:
                if queue[-1][-1] == word[0]:
                    queue.append(word)
                    person += 1

                    if person > n:
                        person = 1
                        order += 1

                else:
                    return [person, order]
            else:
                return [person, order]

    return [0, 0]
