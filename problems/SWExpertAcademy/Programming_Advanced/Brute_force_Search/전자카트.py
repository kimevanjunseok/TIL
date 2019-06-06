import sys
sys.stdin = open("전자카트_input.txt")

def func(x, y, sums):
    global N, minN
    if x == y:
        sums += arr[A[-1]][0]

        if sums < minN:
            minN = sums

    else:
        for i in range(x, y):
            A[x], A[i] = A[i], A[x]
            if sums < minN:
                func(x+1, y, sums + arr[A[x-1]][A[x]])
            A[x], A[i] = A[i], A[x]

T = int(input())

for n in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    A = list(range(N))
    minN = 9999999999999999
    func(1, N, 0)
    print("#{0} {1}".format(n, minN))
