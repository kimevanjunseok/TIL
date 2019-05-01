def QuickSort(start, end):
    if start >= end:
        return
    p, t = end, start
    for i in range(start, end):
        if arr[i] < arr[p]:
            arr[i], arr[t] = arr[t], arr[i]
            t += 1
    arr[p], arr[t] = arr[t], arr[p]
    QuickSort(start, t-1)
    QuickSort(t+1, end)

arr = [100, 89, 23, 111, 1, 5, 78, 3, 44, 44, 56, 1, 90]
QuickSort(0, len(arr)-1)
print(arr)