M = int(input())
arr_M = [list(map(int, list(input()))) for _ in range(M)]

P = int(input())
arr_P = [list(map(int, list(input()))) for _ in range(P)]

result = 0

for i in range(M-P+1):
    save = []
    for j in range(M-P+1):
        save = [arr_M[i][j:j+P]] + [arr_M[i+1][j:j+P]] + [arr_M[i+2][j:j+P]]
        if arr_P == save:
            result += 1

print(result)
