def powerset(x, y):
    global M
    if x == y:
        if t.count(1) == M:
            L = []
            for i in range(y):
                if t[i] == 1:
                    L.append(arr[i])
            if sorted(L) not in result:
                result.append(sorted(L))
    else:
        powerset(x+1, y)
        t[x] = 1
        powerset(x+1, y)
        t[x] = 0

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    result = []
    t = [0] * N
    powerset(0, N)
    print(len(result))
