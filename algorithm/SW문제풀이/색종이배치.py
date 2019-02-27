one = list(map(int, input().split()))
two = list(map(int, input().split()))

arr = [[0 for _ in range(101)] for _ in range(101)]

for i in range(one[0], one[0]+one[2]):
    for j in range(one[1], one[1]+one[3]):
        arr[i][j] = 1

for i in range(two[0], two[0]+two[2]):
    for j in range(two[1], two[1]+two[3]):
        arr[i][j] = 1

area = (one[2] * one[3]) + (two[2] * two[3])
rnd = (one[2] + one[3])*2 + (two[2] + two[3])*2

cnt_area = 0
for i in range(101):
    for j in range(101):
        if arr[i][j] == 1:
            cnt_area += 1
cnt_rnd = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] != arr[i+1][j]:
            cnt_rnd  += 1
        if arr[i][j] != arr[i][j+1]:
            cnt_rnd  += 1

if area != cnt_area:
    print(3)
else:
    if rnd != cnt_rnd :
        print(2)
    else:
        if (list(range(min(one[0], two[0]), max((one[0]+one[2]), (two[0]+two[2])))) == list(set(list(range(one[0], one[0]+one[2])) + list(range(two[0], two[0]+two[2]))))) and (list(range(min(one[1], two[1]), max((one[1]+one[3]), (two[1]+two[3])))) == list(set(list(range(one[1], one[1]+one[3])) + list(range(two[1], two[1]+two[3]))))):
            print(1)
        else:
            print(4)
