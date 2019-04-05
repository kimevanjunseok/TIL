def H(x, y):
    if y == 0:
        print(T)
    elif x == 0:
        return
    else:
        T[y-1] = A[x-1]
        H(x, y-1)
        H(x-1, y)

A =[1,2,3,4]
T =[0] * 3
H(4, 3)
