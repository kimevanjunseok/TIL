T = int(input())
L = [input().split() for _ in range(T)]
result = 10
for i in range(T):
    if int(L[i][0]) >= result and L[i][1] == 'N':
        result = 'F'
        break
    elif int(L[i][0]) < result and L[i][1] == 'Y':
        result = int(L[i][0])
print('F') if result == 10 else print(result)