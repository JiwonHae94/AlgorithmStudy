from itertools import permutations

if __name__ == '__main__':
    n = int(input())
    a_lst = list(map(int, input().split()))
    add, sub, mul, div = map(int, input().split())
    op_total = add + sub + mul + div
    adds = ['+' for _ in range(add)]
    subs = ['-' for _ in range(sub)]
    muls = ['*' for _ in range(mul)]
    divs = ['/' for _ in range(div)]

    op = adds + subs + muls + divs
    op_permut = list(permutations(op, n-1))
    max_num = -1
    min_num = 987654321
    for op_ in op_permut:
        total = a_lst[0]

        for i in range(1, n):
            num = a_lst[i]
            op = op_[i-1]
            if op == '+':
                total += num
            elif op == '-':
                total -= num
            elif op == '*':
                total *= num
            elif op == '/':
                total /= num
                total = int(total)
        if max_num < total:
            max_num = total
        if min_num > total:
            min_num = total
    print(max_num)
    print(min_num)
