def pop(L):
    if len(L) == 0:
        L.append('*')
        return
    return L.pop()

def func(S):
    L = []
    for i in S:
        if i == '(':
            L.append(i)
        else:
            pop(L)
    if len(L) == 0:
        return 1
    return 0


print(func('()()()()(())(())'))
print(func('((()))(())()()'))
print(func('(())())'))
print(func('(())()('))
