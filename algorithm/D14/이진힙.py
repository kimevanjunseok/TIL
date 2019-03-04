import sys
sys.stdin = open("이진힙_input.txt")

T = int(input())

def Treemake():
    global make, arr

    for i in range(1, N+1):
        arr[i][0] = i
        
        if make:
            arr[i][1] = make.pop(0)

        if make:
            arr[i][2] = make.pop(0)


def preorder(node):
    global save
    if node != 0:
        save.append(node)
        preorder(arr[node][1])
        preorder(arr[node][2])



for n in range(1, T+1):
    N = int(input())
    heap_input = [0] + list(map(int, input().split()))
    make = list(range(2, N+1))
    save = []
    arr = [[0, 0, 0] for _ in range(N+1)]

    Treemake()
    preorder(1)

    cnt = 1
    out = 0
    while True:
        
        if arr[cnt][1] == 0 and arr[cnt][2] == 0:
            cnt = 1
            out = 0
        if heap_input[arr[cnt][0]] > heap_input[arr[cnt][1]] or heap_input[arr[cnt][0]] > heap_input[arr[cnt][2]]:
            if heap_input[arr[cnt][1]] < heap_input[arr[cnt][2]]:
                heap_input[arr[cnt][0]], heap_input[arr[cnt][1]] = heap_input[arr[cnt][1]], heap_input[arr[cnt][0]]
            elif heap_input[arr[cnt][1]] > heap_input[arr[cnt][2]]:
                if arr[cnt][2] != 0:
                    heap_input[arr[cnt][0]], heap_input[arr[cnt][2]] = heap_input[arr[cnt][2]], heap_input[arr[cnt][0]]
                else:
                    if heap_input[arr[cnt][0]] > heap_input[arr[cnt][1]]:
                        heap_input[arr[cnt][0]], heap_input[arr[cnt][1]] = heap_input[arr[cnt][1]], heap_input[arr[cnt][0]]
            out += 1
        cnt += 1

        
        if (arr[cnt][1] == 0 and arr[cnt][2] == 0) and not out:
            break

    result = 0
    com = arr[-1][0]

    while True:
        cnt = 0
        for i in arr:
            if i[1] == com or i[2] == com:
                com = i[0]
                result += heap_input[com]
                break
            else:
                cnt += 1
        if cnt == len(arr):
            break

    print(f'#{n} {result}')

