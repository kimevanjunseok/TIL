def binarySearch(a, key):
    start, end = 0, len(a) -1
    while start <= end:
        middle = (start + end) // 2
        if key == a[middle]:
            return middle
        elif key < a[middle]:
            end = middle -1
        else:
            start = middle + 1
    return -1
key = 22
data = [2,4,7,9,11,19,22,23]
print(binarySearch(data, key))