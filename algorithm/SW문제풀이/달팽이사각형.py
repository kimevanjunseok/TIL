n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]

cnt = 1
m = n
x_num, y_num = 0, 0
if not n % 2:
    while cnt != m*m+1:
        x, y = x_num, y_num 

        for i in range(n-1):
            arr[x][y] = cnt
            y += 1
            cnt += 1

        for i in range(n-1):
            arr[x][y] = cnt
            x += 1
            cnt += 1

        for i in range(n-1):
            arr[x][y] = cnt
            y += -1
            cnt += 1

        for i in range(n-1):
            arr[x][y] = cnt
            x += -1
            cnt += 1

        n += -2
        x_num += 1
        y_num += 1

else:
    while cnt != m*m:
        x, y = x_num, y_num 

        for i in range(n-1):
            arr[x][y] = cnt
            y += 1
            cnt += 1

        for i in range(n-1):
            arr[x][y] = cnt
            x += 1
            cnt += 1

        for i in range(n-1):
            arr[x][y] = cnt
            y += -1
            cnt += 1

        for i in range(n-1):
            arr[x][y] = cnt
            x += -1
            cnt += 1

        n += -2
        x_num += 1
        y_num += 1
    arr[m//2][m//2] = m*m


for i in range(m):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()
    