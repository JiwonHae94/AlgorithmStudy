from collections import deque
from itertools import permutations
import copy

MAX_ANS = float("-inf")
MIN_ANS = float("inf")

N = int(input())
numbers = list(map(int, input().split()))

def convert_ops(list):
    order = ["+", "-", "*", "/"]
    op_map = []

    for i in range(len(list)):
        op_map += [order[i]] * list[i]

    return permutations(op_map)

def perform(operations):
    global MAX_ANS, MIN_ANS

    for i in set(operations):
        temp = calcualte(list(i))

        MAX_ANS = max(MAX_ANS, temp)
        MIN_ANS = min(MIN_ANS, temp)

def calcualte(ops):
    stack = deque(copy.deepcopy(numbers))

    while ops:
        op1 = ops.pop(0)
        num1 = stack.popleft()
        num2 = stack.popleft()

        cache = math_op(op1, num1, num2)
        stack.insert(0, cache)

    return stack.pop()


def math_op(op, num1, num2):
    if op == "+":
        return num1 + num2
    elif op =="-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        if num1 < 0:
            return abs(num1)//num2 * -1
        return num1 // num2

operations = convert_ops(list(map(int, input().split())))
perform(operations)
print(MAX_ANS)
print(MIN_ANS)