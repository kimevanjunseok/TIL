def dfs(x, sums):
    global N, minN
    if sums > minN:
        return
        
    if x == N:
        if sums < minN:
            minN = sums
        return 
    value = 0
    for i in range(x+1, N+1):
        if value + arr[i] <= maxN:
            dfs(i, sums + time[i])
            value += arr[i]
        else:
            return

maxN = int(input())
N = int(input())
arr = list(map(int, input().split()))
time = list(map(int, input().split())) + [0]
minN = 10000000000
value = 0
for i in range(N+1):
    if value + arr[i] <= maxN:
        dfs(i, time[i])
        value += arr[i]
    else:
        break
print(minN)
