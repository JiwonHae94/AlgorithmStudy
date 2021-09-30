def grid(m, n, puddles):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    tmp = [m,n]
    if tmp in puddles:
        return 0

    return grid(m-1,n,puddles) + grid(m,n-1,puddles)


def solution(m, n, puddles):
    
    answer = [[0]*m for i in range(n)]
    
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                answer[i][j] = 1
                continue
            tmp = [j+1, i+1]
            if tmp in puddles:
                answer[i][j] = 0
            else:
                answer[i][j] = (answer[i-1][j] + answer[i][j-1]) % 1000000007
                
    return answer[n-1][m-1]

print(solution(4, 3, [[2, 2]]))
