def comb(x, y):
    if y == 0:
        print(T)
    elif x < y:
        return
    else:
        T[y-1] = A[x-1]
        comb(x-1, y-1)
        comb(x-1, y)

A =[1,2,3,4]
T =[0] * 3

comb(4,3)
