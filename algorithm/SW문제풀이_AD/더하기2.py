def bin(x):
    start = 0
    end = len(L)-1
    while start <= end:
        middle = (start + end)//2
        if L[middle] == x:
            return middle+1
        elif L[middle] > x:
            start = middle +1
        else:
            end = middle -1
    return 0

def perm(x, y):
    global N
    if x == y:
        value = 0
        for i in range(N):
            if T[i]:
                value += arr[i]
        if value not in L:
            L.append(value)
    else:
        perm(x+1, y)
        T[x] = True
        perm(x+1, y)
        T[x] = False

N, K = map(int, input().split())
arr = list(map(int, input().split()))
T = [False] * N
L = []
perm(0, N)
L.sort(reverse=True)
print(bin(K))
