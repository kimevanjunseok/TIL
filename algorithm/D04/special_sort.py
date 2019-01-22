import sys
sys.stdin = open("special_sort_input.txt")

T = int(input())

for i in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))
    result = ""
    for j in range(0, len(L)-1, 2):
        max = j
        for k in range(j + 1, len(L)):
            if L[max] < L[k]:
                max = k
        L[j], L[max] = L[max], L[j]

        min = j+1
        for k in range(j + 1, len(L)):
            if L[min] > L[k]:
                min = k
        L[j+1], L[min] = L[min], L[j+1]

    L = L[:10]
    for j in range(len(L)):
        L[j] = f"{L[j]}"
    result = " ".join(L)

    print(f"#{i} {result}")