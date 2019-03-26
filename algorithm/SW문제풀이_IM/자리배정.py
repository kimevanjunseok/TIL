C, R = map(int, input().split())
K = int(input())
if C * R < K:
    print(0)
else:
    x, y = 1, 1
    while True:
        if K > ((C + R) * 2) - 4:
            K = K - (((C + R) * 2) - 4)
            C = C - 2
            R = R - 2
            x += 1
            y += 1
            
        else:
            break
    
    while True:
        for i in range(R-1):
            if K == 1:
                break
            y += 1
            K += -1
        for i in range(C-1):
            if K == 1:
                break
            x += 1
            K += -1
        for i in range(R-1):
            if K == 1:
                break
            y += -1
            K += -1
        for i in range(C-2):
            if K == 1:
                break
            x += -1
            K += -1
        
        if K == 1:
            break
        
        C = C - 2
        R = R - 2
        x = x + 1
        y = y + 1
    print(x, y)
