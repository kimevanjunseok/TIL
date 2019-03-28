def perm(x, y, sums):
    global result

    if x == y:
        if sums < result:
            result = sums
        return
    else:
        for i in range(x, y):
            a[i], a[x] = a[x], a[i]
            if sums + arr[x][a[x]] < result:
                perm(x+1, y, sums + arr[x][a[x]])
            a[i], a[x] = a[x], a[i]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
a = list(range(N))
result = 10000
perm(0, N, 0)
print(result)