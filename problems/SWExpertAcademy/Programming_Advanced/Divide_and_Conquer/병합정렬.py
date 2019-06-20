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
    result = []

    if left[-1] > right[-1]:
        cnt += 1

    while (i < len(left) and (j < len(right))):
        if left[i] <= right[j]:
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