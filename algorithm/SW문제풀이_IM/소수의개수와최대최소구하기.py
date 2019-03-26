a, b = map(int, input().split())

def sosu(N):
    L = [True] * (N+1)
    M = int(N ** 0.5)
    for i in range(2, M+1):
        if L[i] == True:
            for j in range(i+i, N+1, i):
                L[j] = False
    return [i for i in range(2, N+1) if L[i] == True]

sosu_list = sosu(b)
for i in range(len(sosu_list)):
    if sosu_list[i] >= a:
        index = i
        break
sosu_list = sosu_list[index:]
print(len(sosu_list))
print(max(sosu_list)+min(sosu_list))

