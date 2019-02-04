# My solution

def solution(n):
    L = [True] * (n + 1)
    M = int(n**0.5)
    for i in range(2, M+1):
        if L[i] == True:
            for j in range(i+i, n+1 ,i):
                L[j] = False
    return len([i for i in range(2, n+1) if L[i] == True])