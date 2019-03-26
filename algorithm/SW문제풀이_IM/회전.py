n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def result(L):
    global n
    for i in range(n):
        for j in range(n):
            print(L[i][j], end=' ')
        print()


while True:
    S = input()
    if S == '0':
        break

    save = [[0 for _ in range(n)] for _ in range(n)]
    
    if S == '90':
        for i in range(n):
            for j in range(n):
                save[i][j] = arr[n-j-1][i]
    elif S == '180':
        for i in range(n):
            for j in range(n):
                save[i][j] = arr[n-i-1][n-j-1]
    elif S == '270':
        for i in range(n):
            for j in range(n):
                save[i][j] = arr[j][n-i-1]
    elif S == '360':
        save = arr
    
    result(save)

    arr = save