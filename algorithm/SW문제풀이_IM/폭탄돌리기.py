IDX = int(input())
Q_num = int(input())
Q = [input().split() for _ in range(Q_num)]
time = 0
cnt = 0
while True:
    time += int(Q[cnt][0])

    if cnt == len(Q) or time > 210:
        break

    if Q[cnt][1] == 'T':
        IDX += 1

    cnt += 1

    if IDX == 9:
        IDX = 1
    
print(IDX)