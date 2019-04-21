def Mergesort(L):
    if len(L) <= 1: return L

    mid = len(L) // 2
    left = Mergesort(L[:mid])
    right = Mergesort(L[mid:])

    return Merge(left, right)

def Merge(left, right):

    i, j = 0, 0
    result = []

    while (i < len(left)) and (j < len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1

    return result

L = [100, 89, 23, 111, 1, 5, 78, 3, 44, 44, 56, 1, 90]
print(Mergesort(L))