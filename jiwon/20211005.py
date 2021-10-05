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

# -------------------------------------
# category :
# Q : 두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다.
#     예를 들어 2와 7의 최소공배수는 14가 됩니다. 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다.
#     n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.
# url : https://programmers.co.kr/learn/courses/30/lessons/12953
# 설명 : numbers
# --------------------------------------
# space complexity : O(n)
# time complexity : O(n)
def solution(arr):
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    def lcm(a, b):
        t = gcd(a, b)
        return (a // t) * (b // t) * t

    while len(arr) > 1:
        arr.sort()
        arr.append(lcm(arr[0], arr[1]))
        arr.pop(0)
        arr.pop(0)

    return arr[0]


# -------------------------------------
# category :
# Q : 124 나라가 있습니다. 124 나라에서는 10진법이 아닌 다음과 같은 자신들만의 규칙으로 수를 표현합니다.
#     124 나라에는 자연수만 존재합니다.
#     124 나라에는 모든 수를 표현할 때 1, 2, 4만 사용합니다.
#     예를 들어서 124 나라에서 사용하는 숫자는 다음과 같이 변환됩니다.
# url : https://programmers.co.kr/learn/courses/30/lessons/12899
# 설명 : re, python
# --------------------------------------
# space complexity : O(n)
# time complexity : O(log3(n))

def solution(n):
    stack = []

    def convert(n):
        if n < 3:
            if n != 0:
                stack.append(n)
            return
        if n % 3 == 0:
            stack.append(n % 3)
            n -= 1
        else:
            stack.append(n % 3)
        convert(n // 3)

    na = {0: "4", 1: "1", 2: "2"}
    convert(n)
    answer = [na[i] for i in stack]

    return "".join(answer[::-1])

# -------------------------------------
# category :
# Q : 0과 1로 이루어진 문자열 s가 매개변수로 주어집니다.
#     s가 "1"이 될 때까지 계속해서 s에 이진 변환을 가했을 때, 이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수를 각각 배열에 담아
#     return 하도록 solution 함수를 완성해주세요.
# url : https://programmers.co.kr/learn/courses/30/lessons/70129
# 설명 : numbers
# --------------------------------------
# space complexity : O(n)
# time complexity : O(log(n))

def solution(s):
    zero_cnt, num_repeat = 0, 0

    while s != "1":
        num_repeat += 1
        zero_cnt += s.count("0")

        s = s.replace("0", "")
        s = str(bin(len(s)))[2:]

    return [num_repeat, zero_cnt]


# -------------------------------------
# category :
# Q : H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다.
#    어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다.
#    위키백과1에 따르면, H-Index는 다음과 같이 구합니다.
#    어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.
# url : https://programmers.co.kr/learn/courses/30/lessons/42747
# 설명 : numbers
# --------------------------------------
# space complexity : O(n)
# time complexity : O(n)
def solution(citations):
    for i in range(max(citations), -1, -1):
        more_than = [th for th in citations if th >= i]

        if len(more_than) >= i:
            return i
    return 0


# -------------------------------------
# category :
# Q : 셀수있는 수량의 순서있는 열거 또는 어떤 순서를 따르는 요소들의 모음을 튜플(tuple)이라고 합니다. n개의 요소를 가진 튜플을 n-튜플(n-tuple)이라고 하며, 다음과 같이 표현할 수 있습니다.
#     (a1, a2, a3, ..., an)
#     튜플은 다음과 같은 성질을 가지고 있습니다.
#     중복된 원소가 있을 수 있습니다. ex : (2, 3, 1, 2)
#     원소에 정해진 순서가 있으며, 원소의 순서가 다르면 서로 다른 튜플입니다. ex : (1, 2, 3) ≠ (1, 3, 2)
#     튜플의 원소 개수는 유한합니다.
# url : https://programmers.co.kr/learn/courses/30/lessons/64065
# 설명 : string split
# --------------------------------------
# space complexity : O(n)
# time complexity : O(n)
def solution(s):
    s = sorted(s[2:-2].split("},{"), key=len)
    for i in range(len(s)):
        s[i] = list(map(int, s[i].split(",")))

    answer = s[0].copy()

    for j in range(1, len(s)):
        answer += [item for item in s[j] if item not in answer]

    return answer