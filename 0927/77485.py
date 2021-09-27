
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
