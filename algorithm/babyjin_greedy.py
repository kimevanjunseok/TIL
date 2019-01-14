num = 123123
C = [0] * 12
for i in range(6):
    C[num % 10] += 1
    num //= 10
i=0
tri = 0
run = 0
while i < 10:
    if C[i] >= 3:
        C[i] -= 3
        tri += 1
        continue
    if C[i] >= 1 and C[i+1] >= 1 and C[i+2]:
        C[i] -= 1
        C[i+1] -= 1
        C[i+2] -= 1
        run += 1
        continue
    i += 1
if run + tri == 2 : print("Baby Gin")
else : print("Lose")

