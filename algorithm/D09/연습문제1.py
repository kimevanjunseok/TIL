S = "(6+5*(2-8)/2)"

def postfix(S):
    cal = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }
    
    stack = []
    postfix_list = []
    for i in S:
        if i == ')':
            while True:
                postfix_list.append(stack.pop())
                if stack[-1] == '(':
                    stack.pop()
                    break
        elif i == '(':
            stack.append(i)
        elif i in cal:
            if not stack:
                stack.append(i)
            elif stack[-1] == '(' or cal[i] > cal[stack[-1]]:
                stack.append(i)
            else:
                while True:
                    postfix_list.append(stack.pop())
                    if cal[i] > cal[stack[-1]]:
                        stack.append(i)
                        break
        else:
            postfix_list.append(i)
    return postfix_list
print(postfix(S))