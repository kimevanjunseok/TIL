def solution(s):
    stack = []
    for i in range(len(s)):
        if not stack:
            if s[i] == '(':
                stack.append('(')
            else:
                return False
        elif s[i] == '(':
            stack.append('(')
        elif s[i] == ')':
            stack.pop()
    if stack:
        return False
    return True