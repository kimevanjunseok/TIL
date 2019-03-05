import sys
sys.stdin = open("이진탐색_input.txt")

T = int(input())

def Treemake():
    global arr, make

    for i in range(1, N+1):
        arr[i][0] = make.pop(0)
        if not make:
            break
        arr[i][1] = make.pop(0)
        if not make:
            break

def inorder(node):
    if node != 0:
        inorder(arr[node][0])
        save.append(node)
        inorder(arr[node][1])
        

for n in range(1, T+1):
    N = int(input())
    make = list(range(2, N+1))
    arr = [[0, 0] for _ in range(N+1)]
    save = []
    Treemake()
    inorder(1)
    print(save)
    print("#{0} {1} {2}".format(n, save.index(1)+1, save.index(N//2)+1))