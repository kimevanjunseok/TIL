N = int(input())
arr = list(map(int, input().split()))
standard = int(input())
if standard >= sum(arr):
    print(max(arr))
else:
    avg = standard / N
    save1 = []
    save2 = []
    for i in range(N):
        if arr[i] > avg:
            save1.append(arr[i])
        else:
            save2.append(arr[i])

    save1.sort(reverse=True)
    while True:
        maxN = max(save1)
        for i in range(len(save1)):
            if save1[i] == maxN:
                save1[i] += -1
            else:
                break

        if sum(save1) + sum(save2) <= standard:
            break
    print(max(save1))



