# -------------------------------------
# category :
# Q :  보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.
#      예를들어
#      F(2) = F(0) + F(1) = 0 + 1 = 1
#      F(3) = F(1) + F(2) = 1 + 1 = 2
#      F(4) = F(2) + F(3) = 1 + 2 = 3
#      F(5) = F(3) + F(4) = 2 + 3 = 5
#      와 같이 이어집니다.
#      2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.
#      url : https://programmers.co.kr/learn/courses/30/lessons/12945
# 설명 : DP
# --------------------------------------
# space complexity : O(n)
# time complexity : O(n)

def solution(num):
    ans = [0 for i in range(num + 1)]
    ans[1] = 1

    for i in range(2, num + 1):
        ans[i] = ans[i - 1] + ans[i - 2]

    return ans[num] % 1234567

# -------------------------------------
# category :
# Q :  지도개발팀에서 근무하는 제이지는 지도에서 도시 이름을 검색하면 해당 도시와 관련된 맛집 게시물들을 데이터베이스에서 읽어 보여주는 서비스를 개발하고 있다.
#      이 프로그램의 테스팅 업무를 담당하고 있는 어피치는 서비스를 오픈하기 전 각 로직에 대한 성능 측정을 수행하였는데, 제이지가 작성한 부분 중 데이터베이스에서
#      게시물을 가져오는 부분의 실행시간이 너무 오래 걸린다는 것을 알게 되었다.
#
#      어피치는 제이지에게 해당 로직을 개선하라고 닦달하기 시작하였고, 제이지는 DB 캐시를 적용하여 성능 개선을 시도하고 있지만 캐시 크기를 얼마로 해야 효율적인지 몰라 난감한 상황이다.
#      어피치에게 시달리는 제이지를 도와, DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램을 작성하시오.
#      url : https://programmers.co.kr/learn/courses/30/lessons/17680
# 설명 : LRU
# --------------------------------------
# space complexity : O(n)
# time complexity : O(n)

def solution(cacheSize, cities):
    answer = 0
    cache = []

    for i in cities:
        i = i.lower()
        if len(cache) < cacheSize:
            if i in cache:
                answer += 1
                cache.remove(i)
            else:
                answer += 5
            cache.append(i)
        else:
            if i in cache:
                answer += 1
                cache.remove(i)
            else:
                answer += 5
                if cache:
                    cache.pop(0)

            if len(cache) + 1 <= cacheSize:
                cache.append(i)

    return answer

# -------------------------------------
# category :
# Q :  자연수 n이 주어졌을 때, n의 다음 큰 숫자는 다음과 같이 정의 합니다.
#      조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
#      조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
#      조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
#      예를 들어서 78(1001110)의 다음 큰 숫자는 83(1010011)입니다.
#      자연수 n이 매개변수로 주어질 때, n의 다음 큰 숫자를 return 하는 solution 함수를 완성해주세요.
#      url : https://programmers.co.kr/learn/courses/30/lessons/12911
# 설명 : List
# --------------------------------------
# space complexity : O(n)
# time complexity : O(n)
from collections import Counter

def solution(n):
    original = Counter(str(bin(n)))['1']

    while True:
        n += 1
        next_ = Counter(str(bin(n)))['1']
        if original == next_:
            return n



# -------------------------------------
# category :
# Q :  파일명 정렬
#      세 차례의 코딩 테스트와 두 차례의 면접이라는 기나긴 블라인드 공채를 무사히 통과해 카카오에 입사한 무지는 파일 저장소 서버 관리를 맡게 되었다.
#      저장소 서버에는 프로그램의 과거 버전을 모두 담고 있어, 이름 순으로 정렬된 파일 목록은 보기가 불편했다. 파일을 이름 순으로 정렬하면 나중에 만들어진 ver-10.zip이 ver-9.zip보다 먼저 표시되기 때문이다.
#      버전 번호 외에도 숫자가 포함된 파일 목록은 여러 면에서 관리하기 불편했다. 예컨대 파일 목록이 ["img12.png", "img10.png", "img2.png", "img1.png"]일 경우, 일반적인 정렬은 ["img1.png", "img10.png", "img12.png", "img2.png"] 순이 되지만, 숫자 순으로 정렬된 ["img1.png", "img2.png", "img10.png", img12.png"] 순이 훨씬 자연스럽다.
#      무지는 단순한 문자 코드 순이 아닌, 파일명에 포함된 숫자를 반영한 정렬 기능을 저장소 관리 프로그램에 구현하기로 했다.
#      소스 파일 저장소에 저장된 파일명은 100 글자 이내로, 영문 대소문자, 숫자, 공백(" "), 마침표("."), 빼기 부호("-")만으로 이루어져 있다. 파일명은 영문자로 시작하며, 숫자를 하나 이상 포함하고 있다.
#      파일명은 크게 HEAD, NUMBER, TAIL의 세 부분으로 구성된다.
#      url : https://programmers.co.kr/learn/courses/30/lessons/17686
# 설명 : List
# --------------------------------------
# space complexity : O(n)
# time complexity : O(n)

import re
from functools import cmp_to_key

def solution(files):
    answer = []

    def get_num(s):
        num = re.compile("[0-9]+")
        return num.findall(s)[0]

    def get_info(f):
        number = get_num(f)
        num_index = f.index(number)
        head = f[:num_index]
        tail = f[num_index + len(number):]

        return head, number, tail

    def info_compare(a, b):
        if a[0].lower() == b[0].lower():
            return int(int(a[1]) > int(b[1])) - int(int(a[1]) < int(b[1]))
        else:
            return a[0].lower() > b[0].lower()

    for index, file in enumerate(files):
        head, number, tail = get_info(file)
        answer.append([head, number, tail, index])

    info_sort = cmp_to_key(info_compare)
    answer.sort(key=lambda x: x[0].lower())
    answer.sort(key=info_sort)
    answer = ["".join(i[:-1]) for i in answer]

    return answer