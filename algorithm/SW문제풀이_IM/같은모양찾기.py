M = int(input())
arr_M = [list(map(int, list(input()))) for _ in range(M)]

P = int(input())
arr_P_1 = [list(map(int, list(input()))) for _ in range(P)]
arr_P_2 = [[0 for _ in range(P)] for _ in range(P)]
arr_P_3 = [[0 for _ in range(P)] for _ in range(P)]
arr_P_4 = [[0 for _ in range(P)] for _ in range(P)]


for i in range(P):
    for j in range(P):
        arr_P_2[i][j] = arr_P_1[P-i-1][P-j-1]
        arr_P_3[i][j] = arr_P_1[P-j-1][i]
        arr_P_4[i][j] = arr_P_1[j][P-i-1]

result = 0

for i in range(M-P+1):
    save = []
    for j in range(M-P+1):
        save = [arr_M[i+k][j:j+P] for k in range(P)]
        if arr_P_1 == save:
            result += 1
        if arr_P_2 == save:
            result += 1
        if arr_P_3 == save:
            result += 1
        if arr_P_4 == save:
            result += 1

print(result)