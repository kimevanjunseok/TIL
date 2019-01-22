import sys
sys.stdin = open("subset_sum_input.txt")

T = int(input())
A = list(range(1, 13))
n = len(A)
for i in range(1, T+1):
    N, K = map(int, input().split())
    result = 0

    for j in range(1<<n):
        L = []
        for k in range(n):
            if j & (1<<k):
                L.append(A[k])

        if len(L) == N:
            L_sum = 0
            for k in L:
                L_sum += k
            if L_sum == K:
                result += 1

    print(f"#{i} {result}")