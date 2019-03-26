T = int(input())
L = [300, 60, 10]
if T % 10:
    print(-1)
else:
    for i in range(3):
        if T >= L[i]:
            L[i] ,T = f'{T // L[i]}', T % L[i]
        else:
            L[i] = '0'
S = " ".join(L)
print(S)