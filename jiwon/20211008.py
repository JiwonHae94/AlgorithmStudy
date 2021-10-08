# -------------------------------------
# category :
# Q : 0과 1로 이루어진 2n x 2n 크기의 2차원 정수 배열 arr이 있습니다. 당신은 이 arr을 쿼드 트리와 같은 방식으로 압축하고자 합니다. 구체적인 방식은 다음과 같습니다.
#     당신이 압축하고자 하는 특정 영역을 S라고 정의합니다.
#     만약 S 내부에 있는 모든 수가 같은 값이라면, S를 해당 수 하나로 압축시킵니다.
#     그렇지 않다면, S를 정확히 4개의 균일한 정사각형 영역(입출력 예를 참고해주시기 바랍니다.)으로 쪼갠 뒤, 각 정사각형 영역에 대해 같은 방식의 압축을 시도합니다.
#     arr이 매개변수로 주어집니다. 위와 같은 방식으로 arr을 압축했을 때, 배열에 최종적으로 남는 0의 개수와 1의 개수를 배열에 담아서 return 하도록 solution 함수를 완성해주세요.
# url : https://programmers.co.kr/learn/courses/30/lessons/68936
# 설명 : dfs question, polling layer 생각하면서 풀면 개념적으로 접근 가능
# --------------------------------------
# space complexity : O(n)
# time complexity : O(n)

def solution(arr):
    result = compress(arr)
    result = str(result)
    return [result.count("0"), result.count("1")]


def compress(arr):
    if len(arr) == 1:
        return arr

    width = height = len(arr)
    length = width // 2

    if len(set(flatten(arr))) == 1:
        return [flatten(arr)[0]]

    result = []

    for i in range(0, 2):
        for j in range(0, 2):
            result.append(
                compress([sub_mat[j * length:length * (j + 1)] for sub_mat in arr[i * length:length * (i + 1)]]))

    return result


def flatten(arr):
    out = []
    for i in arr:
        out += i
    return out




