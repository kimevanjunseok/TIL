n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
L = [0] * n
game_1 = []
game_2 = []
game_3 = []
for i in range(n):
    game_1.append(arr[i][0])
    game_2.append(arr[i][1])
    game_3.append(arr[i][2])
for i in range(n):
    if game_1.count(game_1[i]) == 1:
        L[i] += game_1[i]
    if game_2.count(game_2[i]) == 1:
        L[i] += game_2[i]
    if game_3.count(game_3[i]) == 1:
        L[i] += game_3[i]

for i in L:
    print(i)
