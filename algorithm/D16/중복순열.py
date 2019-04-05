def PI(x, y):
    if y==0:
        print(t)
    else:
        for i in range(x-1, -1, -1):
            a[i], a[x-1] = a[x-1], a[i]
            t[y-1] = a[x-1]
            PI(x, y-1)
            a[i], a[x - 1] = a[x - 1], a[i]

a = [1,2,3]
t = [0] * 3

PI(3, 2)