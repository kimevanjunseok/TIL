import sys
sys.stdin = open('전기카트_input.txt')

def perm(n ,k):
    global minN

    if n == k:
        sums = 0
        for i in range(len(a)-1):
            sums += arr[a[i]-1][a[i+1]-1]
        if sums < minN:
            minN = sums
    else:
        for i in range(k, n):
            a[i], a[k] = a[k], a[i]
            perm(n, k+1)
            a[i], a[k] = a[k], a[i]

T = int(input())

for n in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    a = list(range(1, N+1)) + [1]
    minN = 99999999999999999999
    perm(N, 1)
    print("#{0} {1}".format(n, minN))
