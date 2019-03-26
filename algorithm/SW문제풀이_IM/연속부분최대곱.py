N = int(input())
arr = [float(input()) for _ in range(N)]
def mul(L):
    num = 1
    for i in L:
        num *= i
    return num
cnt = 0
max_N = 0
com = 0
while cnt != N:
    if (arr[cnt] > 1) or (arr[cnt] < 1 and com <= arr[cnt]):
        if arr[cnt] < 1 and com <= arr[cnt]:
            com = arr[cnt]
        for i in range(cnt, N):
            save = arr[cnt:i+1]
            if save.count(0) > 0:
                break

            if max_N < mul(save):
                max_N = mul(save)
    cnt += 1

print('{0:0.3f}'.format(max_N))
