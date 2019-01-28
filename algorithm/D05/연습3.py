def BruteForce(p, t):
    i = 0
    j = 0
    M = len(p)
    N = len(t)
    L = []
    while i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        elif j == M - 1:
            L.append(i-M+1)
            j = -1
        i = i + 1
        j = j + 1
    if len(L) > 0:
        return L
    else:
        return -1
p = "is"
t = "This is a book. This is a computer."
print(BruteForce(p, t))