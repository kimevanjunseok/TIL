import sys
sys.stdin = open("병합정렬_input.txt")

def Mergesort(L):
    if len(L) <= 1: return L
    
    mid = len(L) // 2
    left = Mergesort(L[:mid])
    right = Mergesort(L[mid:])

    return Merge(left, right)

def Merge(left, right):
    global cnt

    i, j = 0, 0
    left_len, right_len = len(left), len(right)
    result = []

    if left[left_len - 1] > right[right_len - 1]:
        cnt += 1

    while (i < left_len) and (j < right_len):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < left_len:
        result.append(left[i])
        i += 1

    while j < right_len:
        result.append(right[j])
        j += 1
    
    # result += left[i:]
    # result += right[j:]

    return result


T = int(input())

for n in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    result = Mergesort(arr)
    print("#{0} {1} {2}".format(n, result[N//2], cnt))