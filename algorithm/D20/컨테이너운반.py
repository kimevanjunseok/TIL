import sys
sys.stdin = open("컨테이너운반_input.txt")

T = int(input())

for n in range(1, T+1):
    N, M = map(int, input().split())
    arrN = list(map(int, input().split()))
    arrM = list(map(int, input().split()))
    arrN.sort(reverse=True)
    arrM.sort(reverse=True)
    result = 0
    idx = 0
    for i in range(len(arrM)):
        for j in range(idx, len(arrN)):
            if arrM[i] >= arrN[j]:
                result += arrN[j]
                idx = j+1
                break
    print(result)
