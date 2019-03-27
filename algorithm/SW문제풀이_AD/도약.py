def bin(z, y, s):
    start, end = y + 1, len(arr)-1
    while start <= end:
        middle = (start + end) // 2
        if arr[middle] == z:
            return middle
        elif arr[middle] > z:
            end = middle-1
        elif arr[middle] < z:
            start = middle+1

    if s == "a":
        if arr[middle] > z:
            return middle
        else:
            return middle + 1

    elif s == "b":
        if arr[middle] > z:
            return middle - 1
        else:
            return middle

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
result = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        a = bin(arr[j]*2-arr[i], j, "a")
        b = bin((arr[j] - arr[i])*2+arr[j], j, "b")
        if b >= a:
            result += b - a + 1
print(result)


##############################################################################################
def binary(s,e, data):
    sol = -1
    while s<=e:
        m = (s+e) // 2
        # data 보다 작은 값중에서 가장 큰 값의 위치 찾기
        # data 보다 작으면 오른쪽 영역 재탐색
        if arr[m] < data:
            s = m+1
            sol = m
        # 아니면 (크거나 같으면) 왼쪽 영역 재탐색
        else:
            e = m-1
    return sol # 못찾았으면 -1 리턴

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()

sol = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        start = arr[j] + (arr[j] - arr[i])    # 5
        end = arr[j] + (arr[j] - arr[i]) * 2 +1 # 7
        lo = binary(j, N-1, start)
        up = binary(j, N-1, end)
        sol += (up-lo)

print(sol)

#################################################################################################
def lowerSearch(s, e, data):
    sol = -1
    while s <= e:
        m = (s+e)//2
        if arr[m] >= data:
            sol = m
            e = m-1
        else: s = m+1
    return sol
def upperSearch(s, e, data):
    sol = -1
    while s<=e:
        m = (s+e)//2
        if arr[m] <= data:
            sol = m
            s = m+1
        else: e = m-1
    return sol
N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
arr.sort()
cnt = 0
for i in range(N-2):
    for j in range(N-1):
        start = arr[j] + (arr[j]-arr[i])
        end = arr[j] + (arr[j]-arr[i])*2
        lo = lowerSearch(j+1, N-1, start)
        if lo==-1 or arr[lo]>end: continue
        up = upperSearch(j+1, N-1, end)
        cnt += (up-lo+1)
print(cnt)