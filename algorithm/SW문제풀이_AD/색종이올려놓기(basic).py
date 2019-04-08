def dfs(L):
    global result
    if len(L) > result:
        result = len(L)

    for i in range(len(arr)):
        if arr[i] not in L and ((L[-1][0] >= arr[i][0] and L[-1][1] >= arr[i][1]) or (L[-1][1] >= arr[i][0] and L[-1][0] >= arr[i][1])):
            L.append(arr[i])
            dfs(L)
            L.pop()


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
stack = []
result = 0
for i in range(len(arr)):
    stack.append(arr[i])
    dfs(stack)
    stack.pop()
print(result)