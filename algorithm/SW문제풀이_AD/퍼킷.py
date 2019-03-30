def perm(x, y):
    global N, minN
    if x == y:
        value1 = 1
        value2 = 0
        if T.count(1) >= 1:
            for i in range(N):
                if T[i] == 1:
                    value1 *= arr[i][0]
                    value2 += arr[i][1]

            if abs(value1 - value2) < minN:
                minN = abs(value1 - value2)

    else:
        perm(x+1, y)
        T[x] = 1
        perm(x+1, y)
        T[x] = 0

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
T = [0] * N
minN = 1000000000000000
perm(0, N)
print(minN)