def perm(x, y, L, S):
    global N
    if x == y:
        value = 0
        if T.count(1) >= 2:
            for i in range(N):
                if T[i] == 1:
                    if not value:
                        value = L[i]
    
                    elif S == "S":
                        value = value*L[i]
                    else:
                        value = value+L[i]
            if S == "S":
                if value not in S1:
                    S1.append(value)
            else:
                if value not in B1:
                    B1.append(value)

                
    else:
        perm(x+1, y, L, S)
        T[x] = 1
        perm(x+1, y, L, S)
        T[x] = 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
S, B = [], []
for i in range(N):
    S.append(arr[i][0])
    B.append(arr[i][1])

T = [0] * N
S1 = []
B1 = []
perm(0, N, S, "S")
perm(0, N, B, "B")
minN = 1000000000000000
for i in range(len(S1)):
    for j in range(len(B1)):
        if abs(S1[i] - B1[j]) < minN:
            minN = abs(S1[i] - B1[j])
print(S1)
print(B1)

print(minN)


