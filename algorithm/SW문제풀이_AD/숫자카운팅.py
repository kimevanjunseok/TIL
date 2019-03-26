def bin(x):
    start, end = 0, len(arrN) -1
    while start <= end:
        middle = (start + end) // 2
        if arrN[middle] == x:
            return arrN.count(x)
        elif arrN[middle] < x:
            start = middle +1
        elif arrN[middle] > x:
            end = middle -1
    return 0

N = int(input())
arrN = list(map(int, input().split()))
M = int(input())
arrM = list(map(int, input().split()))

for i in range(len(arrM)):
    print(bin(arrM[i]), end=" ")