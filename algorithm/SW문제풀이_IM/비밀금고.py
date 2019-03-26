N = int(input())
L = list(map(int, input().split()))
arr = [[0 for _ in range(N+N-1)] for _ in range(N+N-1)]
cnt = (2 * N -1) // 2
index = cnt
count = 1
for i in range(len(arr)):

    for k in range(count):
        arr[i][index] = L.pop(0)
        index += 2

    if i >= ((2 * N -1) // 2):
        cnt += 1
        index = cnt
        count += -1
    else:
        cnt += -1
        index = cnt
        count += 1

result = 0
for i in range(len(arr)):
    max_num = 0
    for j in range(len(arr)):
        max_num += arr[j][i]
    if result < max_num:
        result = max_num

print(result)