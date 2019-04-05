def perm(x, y):
    if x == y:
        print(a)
    else:
        for i in range(x, y):
            a[i], a[x] = a[x], a[i]
            perm(x+1, y)
            a[i], a[x] = a[x], a[i]

a = [1,2,3,4,5]
perm(0, len(a))
