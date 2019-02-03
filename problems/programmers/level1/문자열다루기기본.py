# My solution

def solution(s):
    L = list(range(10)) * 6
    if len(s) == 4:
        for i in L:
            s = s.replace(str(i), '')
    else:
        return False
    return not s