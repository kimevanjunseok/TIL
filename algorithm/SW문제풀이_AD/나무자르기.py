def cut(x, value):
    global M
    sums = 0
    for i in range(x, len(arr)):
        sums += (arr[i] - value)
    return sums



def bin(x):
    start, end = 0, len(arr)
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < x:
            start = mid + 1
        else:
            sol = mid
            end = mid - 1
    return sol

N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
arr.sort()
start, end = min(arr), max(arr)
while start <= end:
    mid = (start + end) // 2
    x = bin(mid)
    value = cut(x, mid)
    if value == M:
        result = mid
        break
    elif value < M:
        result = mid - 1
        end = mid - 1
    else:
        start = mid + 1
print(result)
