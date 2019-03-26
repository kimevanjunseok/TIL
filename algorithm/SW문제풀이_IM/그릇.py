T = input()
cnt = 10
for i in range(1, len(T)):
    if T[i-1] != T[i]:
        cnt += 5
    cnt += 5
print(cnt)