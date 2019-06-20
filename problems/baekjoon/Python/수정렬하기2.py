import sys

N = int(input())
even = []
odd = []
for i in range(N):
    n = int(sys.stdin.readline())
    if n % 2:
        odd.append(n)
    else:
        even.append(n)

odd.sort()
even.sort()

i, j = 0, 0

while (i < len(odd) and j < len(even)):
    if odd[i] < even[j]:
        print(odd[i])
        i += 1
    else:
        print(even[j])
        j += 1

if i == len(odd):
    while j < len(even):
        print(even[j])
        j += 1
else:
    while i < len(odd):
        print(odd[i])
        i += 1