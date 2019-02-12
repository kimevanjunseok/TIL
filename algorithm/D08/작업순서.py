import sys
sys.stdin = open("작업순서_input.txt")

T = 6

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
    cnt = 1
    result = []
    road = []
    copy_L = L
    while len(road) != V:

        copy = []
        if cnt == 1:
            for i in range(len(L)):

                if L[i][0] in work:
                    road += L[i]
                    copy_L.remove(L[i])
                    copy += [L[i][1]]   
        else:
            for i in range(len(L)):
                if L[i][0] in work:
                    road += L[i][1]
                    copy_L.remove(L[i])
                    copy += [L[i][1]]
        work = copy
        L = copy_L
        cnt += 1



        

        
    
    