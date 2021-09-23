
# -----------------------
# category : 연습문제, array
# Q : 정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.
# url : https://programmers.co.kr/learn/courses/30/lessons/12944
# 설명 : 평균 = list의 합 / list안의 item 수
def solution(arr):
    return sum(arr) / len(arr)


##########
# 정해진 기간 (max 이릍) 내 답변을 풀지 못한 경우
# 아래와 같이 다른 사람의 답변을 복붙 하시고,
# 커밋 메시지에 표기
import statistics

def average(list):
    # 함수를 완성해서 매개변수 list의 평균값을 return하도록 만들어 보세요.
    return statistics.mean(list)