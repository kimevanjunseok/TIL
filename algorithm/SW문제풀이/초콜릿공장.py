N = int(input())
arr = [input().split() for _ in range(N)]
al = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
result = 0
for i in arr:
    if len(set(i[0]) & set(i[1])) > 2:
        result += 1
    else:
        for j in al:
            if i[0].count(j) > 1:
                result += 1
                break

            if i[1].count(j) > 1:
                result += 1
                break

print(result)