import sys
sys.stdin = open('Forth_input.txt')

def machine(x, y, s):
    if s == '+':
        return int(x) + int(y)
    elif s == '-':
        return int(x) - int(y)
    elif s == '/':
        return int(x) // int(y)
    elif s == '*':
        return int(x) * int(y)

T = int(input())
cal = ['+', '-', '/', '*']

for n in range(1, T+1):
    S = input().split()
    stack = []
    for i in S:
        if i in cal:
            if len(stack) < 2:
                result = 'error'
                break
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(machine(b, a, i))
        elif i == '.':
            if len(stack) > 1:
                result = 'error'
                break
            result = stack.pop()
        else:
            stack.append(i)
    print(f'#{n} {result}')