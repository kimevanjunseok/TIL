def dfs1(x):
    global N
    if x == N:
        dfs2(0)

    else:
        if not L:
            dfs1(x+1)
            L.append(x)
            dfs1(x+1)
            L.pop()
        else:
            if arr[x] < arr[L[-1]]:
                dfs1(x+1)
                L.append(x)
                dfs1(x+1)
                L.pop()
            else:
                dfs1(x+1)

def dfs2(x):
    global N, maxN
    if x in L:
        dfs2(x+1)

    elif x == N:
        a = 0
        b = 0
        for i in L:
            a += arr[i]
        for i in Lreverse:
            b += arr[i]
        if a+b > maxN:
            # print(1, Lreverse)
            # print(2, L)
            maxN = a+b

    else:
        if not Lreverse:
            dfs2(x+1)
            Lreverse.append(x)
            dfs2(x+1)
            Lreverse.pop()
        else:
            if arr[x] > arr[Lreverse[-1]]:
                dfs2(x+1)
                Lreverse.append(x)
                dfs2(x+1)
                Lreverse.pop()
            else:
                dfs2(x+1)

T = int(input())

for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    L = []
    Lreverse = []
    maxN = 0
    dfs1(0)
    print(maxN)



