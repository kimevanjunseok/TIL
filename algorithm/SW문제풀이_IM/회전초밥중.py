N, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr = arr + arr[:k-1]
length = len(arr)
save = arr[:k]
max_num = len(set(save + [c]))
max_max = len(set(arr + [c]))
for i in range(k, length):
    save.pop(0)
    if arr[i] in save:
        save.append(arr[i])
        continue
    else:
        save.append(arr[i])
        if max_num < len(set(save + [c])):
            max_num = len(set(save + [c]))

print(max_num)


