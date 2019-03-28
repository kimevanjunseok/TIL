def perm(x, y, sums):
    global second
    if x == y:
        if sums < second:
            second = sums
    else:
        for i in range(x, y):
            a[i], a[x] = a[x], a[i]
            if sums + arr[x][a[x]] < second:
                perm(x+1, y, sums + arr[x][a[x]])
            a[i], a[x] = a[x], a[i]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
first = 0
second = 10000
a = list(range(N))
for i in arr:
    first += min(i)
perm(0, N, 0)
print(first)
print(second)