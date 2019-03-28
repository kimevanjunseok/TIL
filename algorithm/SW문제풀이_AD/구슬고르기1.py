def perm(x, y):
    if x == y:
        for i in range(len(a)):
            if T[i] == True:
                print(a[i], end=" ")
            else:
                print(0, end=" ")
        print()
        return
    else:
        for i in range(2):
            if i == 0:
                perm(x+1, y)
            else:
                T[x] = False
                perm(x+1, y)
                T[x] = True

N = 3
T = [True] * N
a = list(range(1, N+1))
perm(0, N)
