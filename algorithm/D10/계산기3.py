import sys
sys.stdin = open('계산기3_input.txt')

T = 10

def machine(x, y, s):
    if s == '+':
        return int(x) + int(y)
    elif s == '*':
        return int(x) * int(y)

def postfix(S):
    global stack, postfix

    D = {
        "(": 0,
        "+": 1,
        "*": 2
    }

    for i in S:
        if i == "(":
            stack.append(i)
        elif i == ")":
            while True:
                postfix_list.append(stack.pop())
                if stack[-1] == '(':
                    stack.pop()
                    break
        elif i in D:
            if not stack:
                stack.append(i)
            elif stack[-1] == '(' or D[i] > D[stack[-1]]:
                stack.append(i)
            else:
                while True:
                    postfix_list.append(stack.pop())
                    if D[i] > D[stack[-1]]:
                        stack.append(i)
                        break
        else:
            postfix_list.append(i)
    string = "".join(postfix_list)
    return string

def postfix_cal(S):
    global stack
    cal = ['+', '*']
    for i in S:
        if i in cal:
            stack.append(machine(stack.pop(), stack.pop(), i))
        else:
            stack.append(i)
    return stack[0]


for n in range(1, T+1):
    N = int(input())
    S = input()
    stack = []
    postfix_list = []
    print(f"#{n} {postfix_cal(postfix(S))}")
      