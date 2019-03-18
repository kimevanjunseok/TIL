import sys
sys.stdin = open("단순2진암호코드_input.txt")

T = int(input())

for n in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    for i in arr:
        if "1" in i:
            S = i
            break

    for i in range(len(S)-1, -1, -1):
        if S[i] == "1":
            idx = i
            break
    S = S[i-56:i+1]
    cnt = 0
    L = []
    while cnt < len(S):
        if S[cnt:cnt+7] == "0001101":
            L.append(0)
            cnt += 7
        elif S[cnt:cnt+7] == "0011001":
            L.append(1)
            cnt += 7
        elif S[cnt:cnt+7] == "0010011":
            L.append(2)
            cnt += 7
        elif S[cnt:cnt+7] == "0111101":
            L.append(3)
            cnt += 7
        elif S[cnt:cnt+7] == "0100011":
            L.append(4)
            cnt += 7
        elif S[cnt:cnt+7] == "0110001":
            L.append(5)
            cnt += 7
        elif S[cnt:cnt+7] == "0101111":
            L.append(6)
            cnt += 7
        elif S[cnt:cnt+7] == "0111011":
            L.append(7)
            cnt += 7
        elif S[cnt:cnt+7] == "0110111":
            L.append(8)
            cnt += 7
        elif S[cnt:cnt+7] == "0001011":
            L.append(9)
            cnt += 7
        else:
            cnt += 1

    even = []
    odd = []
    for i in range(len(L)):
        if i%2:
            even.append(L[i])
        else:
            odd.append(L[i])
    print("#{0}".format(n), end=" ")
    print(sum(L)) if not (sum(even) + sum(odd)*3) % 10 else print(0)
