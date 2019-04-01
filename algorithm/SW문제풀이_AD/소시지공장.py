def gogo(List, x):
    global minN
    if len(List) == 1:
        if minN > x:
            minN = x
        return
    elif len(List) < 1:
        if minN > x-1:
            minN = x-1
        return
    N = len(List)
    List.sort()
    L = List[0]
    com1 = []
    for i in range(1, N):
        if L[0] > List[i][0] or L[1] > List[i][1]:
            com1.append(List[i])
        else:
            L = List[i]

    List.sort(key=lambda x: x[1])
    L = List[0]
    com2 = []
    for i in range(1, N):
        if L[0] > List[i][0] or L[1] > List[i][1]:
            com2.append(List[i])
        else:
            L = List[i]

    if len(com1) > len(com2):
        gogo(com2, x + 1)
    elif len(com1) < len(com2):
        gogo(com1, x + 1)
    else:
        gogo(com1, x + 1)
        gogo(com2, x + 1)

N = int(input())
arr = list(map(int, input().split()))
save = []
for i in range(0, N*2, 2):
    save.append([arr[i], arr[i+1]])
minN = 999999999999999
gogo(save, 1)
print(minN)




