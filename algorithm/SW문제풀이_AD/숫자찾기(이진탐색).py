def bin(x):
    start, end = 0, len(arrN)-1
    while start <= end:
        middle = (start + end) // 2
        if arrN[middle] == x:
            return middle+1
        elif arrN[middle] > x:
            end = middle-1
        elif arrN[middle] < x:
            start = middle+1
    return 0

N = int(input())
arrN = list(map(int, input().split()))
T = int(input())
arrT = list(map(int, input().split()))
for i in range(len(arrT)):
    print(bin(arrT[i]))
