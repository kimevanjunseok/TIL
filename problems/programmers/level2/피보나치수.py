# My solution

def solution(n):
    
    stack = [0, 1]

    for i in range(n-1):
        stack.append(stack[i] + stack[i+1])

    return stack[-1] % 1234567