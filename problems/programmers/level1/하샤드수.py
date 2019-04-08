# My solution

def solution(x):
    L = []
    calc = x
    for i in range(len(str(calc))):
        L.append(calc % 10)
        calc = calc // 10
    if x % sum(L) == 0:
        return True
    else:
        return False