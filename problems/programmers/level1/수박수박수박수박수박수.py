# My solution

def solution(n):
    s = ""
    for i in range(1, n+1):
        if i % 2 == 1:
            s += "수"
        else:
            s += "박"
    return s