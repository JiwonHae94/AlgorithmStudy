def grid(m, n, puddles):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    tmp = [m,n]
    if tmp in puddles:
        return 0

    return grid(m-1,n,puddles) + grid(m,n-1,puddles)


def solution(m, n, puddles):0

    answer = grid(m,n,puddles)
    return answer


