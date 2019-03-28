def fibo(x=3):
    global N
    if N < 3:
        return fi[0]
    fi.append(fi[-1] + fi[-2])
    if x == N:
        return fi[-1]
    return fibo(x+1)

N = int(input())
fi = [1, 1]
print(fibo())