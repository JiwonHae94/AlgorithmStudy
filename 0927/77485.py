"""문제 설명
rows x columns 크기인 행렬이 있습니다. 행렬에는 1부터 rows x columns까지의 숫자가 한 줄씩 순서대로 적혀있습니다. 이 행렬에서 직사각형 모양의 범위를 여러 번 선택해, 테두리 부분에 있는 숫자들을 시계방향으로 회전시키려 합니다. 각 회전은 (x1, y1, x2, y2)인 정수 4개로 표현하며, 그 의미는 다음과 같습니다.

x1 행 y1 열부터 x2 행 y2 열까지의 영역에 해당하는 직사각형에서 테두리에 있는 숫자들을 한 칸씩 시계방향으로 회전합니다.
다음은 6 x 6 크기 행렬의 예시입니다.

https://programmers.co.kr/learn/courses/30/lessons/77485

설명 : 뭔지 모르겟음 그냥 노가다로 품

#space complexity : O(n2) ??
#time complextity : O(n) ??

"""

def solution(rows, columns, queries):
    answer = []
    table = []
    for r in range(rows): #2d array 생성
        table.append([a for a in range(r * columns + 1, (r + 1) * columns + 1)])

    for query in queries:
        query = [x - 1 for x in query]  # indexing -1
        first_value = table[query[0]][query[1]]  # 왼쪽 위 값 저장(예외처리)
        small = first_value  # 첫번째 값

        ### left
        for i in range(query[0] + 1, query[2] + 1):
            table[i - 1][query[1]] = table[i][query[1]]
            small = min(small, table[i][query[1]])
        # down
        for i in range(query[1] + 1, query[3] + 1):
            table[query[2]][i - 1] = table[query[2]][i]
            small = min(small, table[query[2]][i])
        # right
        for i in range(query[2] - 1, query[0] - 1, -1):
            table[i + 1][query[3]] = table[i][query[3]]
            small = min(small, table[i][query[3]])
        # udder
        for i in range(query[3] - 1, query[1] - 1, -1):
            table[query[0]][i + 1] = table[query[0]][i]
            small = min(small, table[query[0]][i])
        table[query[0]][query[1] + 1] = first_value

        answer.append(small)

    return answer

rows = 5
columns =6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]

print(solution(rows,columns,queries))
