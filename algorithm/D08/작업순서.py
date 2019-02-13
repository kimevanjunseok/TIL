import sys
sys.stdin = open("작업순서_input.txt")

T = 10

for n in range(1, T+1):
    V, E = map(int, input().split())
    route = list(map(int, input().split()))
    L = []
    
    for i in range(0, len(route), 2):
        L += [[route[i], route[i+1]]]

    work = list(range(1, V+1))

    for i in L:
        if i[1] in work:
            work.remove(i[1])

    result = work

    while L:
        long_L = len(L)
        save = []

        for i in range(long_L):
            if L[i][0] in work:
                save += [L[i]]

        for i in save:
            L.remove(i)

        work = list(range(1, V+1)) 

        for i in L:
            if i[1] in work:
                work.remove(i[1])

        for i in work:
            if i not in result:
                result += [i]

    for i in range(len(result)):
        result[i] = f'{result[i]}'
        
    result = " ".join(result)
    
    print(f"#{n} {result}")

