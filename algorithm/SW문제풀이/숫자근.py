T = int(input())
L = [int(input()) for _ in range(T)]
save = []
for i in range(len(L)):
    save_num = sum(list(map(int, list(str(L[i])))))
    while save_num >= 10:
        save_num = sum(list(map(int, list(str(save_num)))))
    save.append(save_num)
    if save[-1] >= 10:
        save[-1] = save[-1] % 10 + save[-1] // 10
max_idx = 0
max = 0
for i in range(len(save)):
    if max < save[i]:
        max = save[i]
        max_idx = i
    elif max == save[i]:
        if L[i] < L[max_idx]:
            max_idx = i
print(L[max_idx])