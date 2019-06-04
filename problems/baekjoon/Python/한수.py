N = int(input())
if N < 100:
    print(N)
else:
    cnt = 99
    for i in range(100, N+1):
        L = list(str(i))
        D = []
        for j in range(len(L)-1):
            D.append(int(L[j]) - int(L[j+1]))

        if len(D) == D.count(D[0]):
            cnt += 1
    print(cnt)