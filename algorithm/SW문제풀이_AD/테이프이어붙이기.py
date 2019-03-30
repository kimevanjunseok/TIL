def com(x, y):
    global minN
    if y == 0:
        if abs(sum(T) - (sum(arr) - sum(T))) < minN:
            minN = abs(sum(T) - (sum(arr) - sum(T)))
    elif x < y:
        return
    else:
        T[y-1] = arr[x-1]
        com(x-1, y-1)
        com(x-1, y)

N = int(input())
arr = list(map(int, input().split()))
minN = 1000000
T = [0] * (N//2)
com(N, N//2)
print(minN)