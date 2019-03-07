N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(N-K+1):
    for j in range(N-K+1):
        cnt = 0
        for k in range(i, i+K):
            for m in range(j, j+K):
                if (k == i or k == i+K-1) or (m == j or m == j+K-1):
                    cnt += arr[k][m]
                    if result < cnt:
                        result = cnt
print(result)

