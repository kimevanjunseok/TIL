N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()

w = []
h = []
for i in arr:
    w.append(i[0])
    h.append(i[1])
print(w)
print(h)


print(arr)