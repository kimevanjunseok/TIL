N = int(input())
arr = list(map(int, input().split()))
result = 0
while len(arr) != 1:
    arr.sort()
    v1 = arr.pop(0)
    v2 = arr.pop(0)
    result += v1 + v2
    arr = [v1 + v2] + arr

print(result)
