N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
maxN = 0
for i in range(N):
    com = -1000
    cnt = 1
    for j in range(N):
        if com == -1000:
            com = arr[i][j]
        else:
            if arr[i][j] - com == 1:
                cnt += 1
                if maxN < cnt:
                    maxN = cnt 
            else:
                cnt = 1
            
            com = arr[i][j]
            
for i in range(N):
    com = -1000
    cnt = 1
    for j in range(N):
        if com == -1000:
            com = arr[i][j]
        else:
            if com - arr[i][j] == 1:
                cnt += 1
                if maxN < cnt:
                    maxN = cnt 
            else:
                cnt = 1
            
            com = arr[i][j]

for i in range(N):
    com = -1000
    cnt = 1
    for j in range(N):
        if com == -1000:
            com = arr[j][i]
        else:
            if arr[j][i] - com == 1:
                cnt += 1
                if maxN < cnt:
                    maxN = cnt 
            else:
                cnt = 1
            
            com = arr[j][i]

for i in range(N):
    com = -1000
    cnt = 1
    for j in range(N):
        if com == -1000:
            com = arr[j][i]
        else:
            if com - arr[j][i] == 1:
                cnt += 1
                if maxN < cnt:
                    maxN = cnt 
            else:
                cnt = 1
            
            com = arr[j][i]

print(maxN)
