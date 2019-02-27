Y, X = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(Y)]
for i in range(Y):
    cnt = 0
    for j in range(X):
        if arr[i][j] != 0:
            cnt += 1
            if cnt > 1:
                arr[i][j] = cnt
        else:
            cnt = 0
for i in range(Y):
    for j in range(X):
        print(arr[i][j], end=" ")
    print()