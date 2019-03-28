def perm(x, y):
    if x == y:
        L.append([a[i] for i in range(N)])
    else:
        for i in range(x, y):
            a[i], a[x] = a[x], a[i]
            perm(x+1, y)
            a[i], a[x] = a[x], a[i]

N = 3
a = [1, 2, 3]
L = []
perm(0, N)
L.sort()
for i in L:
    print(*i)
