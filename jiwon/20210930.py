
# -------------------------------------
# category :
# Q : 압축할 문자열 s가 매개변수로 주어질 때,
#     위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라 압축하여
#     표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution 함수를 완성해주세요.
# url : https://programmers.co.kr/learn/courses/30/lessons/60057
# 설명 : array,
# --------------------------------------
# space complexity : O(1) -> 추가 메모리 사용 없음
# time complexity : O( n/2 + n) -> O(n)할때 루프

def solution(s):
    answer = len(s)

    for num_char in range(1, len(s) // 2 + 1):
        temp = s[:num_char]
        cnt = 1
        current = ""

        for j in range(num_char, len(s) + num_char, num_char):
            if temp == s[j:j + num_char]:
                cnt += 1
            else:
                if cnt == 1:
                    current += temp
                else:
                    current += str(cnt) + temp

                temp = s[j:j + num_char]
                cnt = 1
        answer = min(answer, len(current))

    return answer
