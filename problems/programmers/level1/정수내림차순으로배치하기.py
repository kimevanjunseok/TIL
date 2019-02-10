# My solution

def solution(n):
    L = [i for i in str(n)]
    L.sort(reverse=True)
    return int("".join(L))