N = int(input())
students = list(map(int, input().split()))
L = []
for idx, i in enumerate(students):
    L.append([idx+1, i])

line = [L[0][0]]
for i in range(1, len(L)):
    line.insert(L[i][1], L[i][0])
line.reverse()
print(*line)